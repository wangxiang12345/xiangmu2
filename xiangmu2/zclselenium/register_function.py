#coding=utf-8
from selenium import webdriver
import time
from xiangmu2.zclselenium.find_element import FindElement
#生成随机用户名
from PIL import Image
from ShowapiRequest import ShowapiRequest
import random
class Regiser_Function:
    def __init__(self,url):
        self.driver=self.get_driver(url)
#获取dirver并且打开url
    def get_driver(self,url):
        driver=webdriver.Chrome()
        driver.get(url)
        time.sleep(5)
        driver.maximize_window()
        return  driver
#输入用户信息
    def send_user_info(self,key,data):
        self.get_user_element(key).send_keys(data)

#获取用户定位信息
    def get_user_element(self,key):
        find_element=FindElement(self.driver)
        user_element=find_element.get_element(key)
        return user_element

    # 生成用户随机数
    def get_range_user(self):
        user_info = ''.join(random.sample('123456789abcdefghijklmnopqrstuvwsyz', 8))
        return user_info

    # 获取图片
    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.get_user_element('code_image')
        print(code_element.location)
        left = code_element.location['x']
        top = code_element.location['y']
        length = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left, top, length, height))
        img.save(file_name)

    # 解析图片获取验证码
    def code_online(self,file_name):
        r = ShowapiRequest("http://route.showapi.com/184-1", "94740", "89a85a49bc6c4507b0d24c7e83096ef8")
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addFilePara("image", file_name)  # 文件上传时设置
        res = r.post()
        text = res.json()['showapi_res_body']['Result']
        return text
    #运行程序
    def main_init(self):
        user_name=self.get_range_user()
        user_email = self.get_range_user() + "@163.com"
        file_name='E:/test/imooc.png'
        print(user_email,user_name)
        self.send_user_info('user_email',user_email)
        self.send_user_info('user_name',user_name)
        self.send_user_info('password',user_name)
        self.get_code_image(file_name)
        text = self.code_online(file_name)
        self.send_user_info('code_text',text)
        self.get_user_element('register_button').click()
        text_error=self.get_user_element('code_text_error')
        if text_error==None:
            print('注册成功')
        else:
            self.driver.save_screenshot('E:/test/text_error.pug')
            print('验证码输入错误')
if __name__ == '__main__':
    regiser_function=Regiser_Function("http://www.5itest.cn/register")
    regiser_function.main_init()
