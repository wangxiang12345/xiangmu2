#coding=utf-8
from   selenium import webdriver
import time
import random
from PIL import Image
from ShowapiRequest import ShowapiRequest
driver=webdriver.Chrome()
#浏览器初始化
def driver_init():
    driver.get('http://www.5itest.cn/register')
    driver.maximize_window()
    time.sleep(5)
#获取element信息
def get_element(id):
    element=driver.find_element_by_id(id)
    return element
#生成用户随机数
def get_range_user():
    user_info=''.join(random.sample('123456789abcdefghijklmnopqrstuvwsyz',8))
    return user_info
#获取图片
def get_code_image(file_name):
    driver.save_screenshot(file_name)
    code_element = driver.find_element_by_id('getcode_num')
    print(code_element.location)
    left = code_element.location['x']
    top = code_element.location['y']
    length = code_element.size['width'] + left
    height = code_element.size['height'] + top
    im = Image.open(file_name)
    img = im.crop((left, top, length, height))
    img.save(file_name)
#解析图片获取验证码
def code_online(file_name):
    r = ShowapiRequest("http://route.showapi.com/184-1", "94740", "89a85a49bc6c4507b0d24c7e83096ef8")
    r.addBodyPara("typeId", "35")
    r.addBodyPara("convert_to_jpg", "0")
    r.addFilePara("image", file_name) # 文件上传时设置
    res = r.post()
    text = res.json()['showapi_res_body']['Result']
    return text
#运行主程序
def run_main():
    driver_init()
    user_email=get_range_user()+'@163.com'
    get_element('register_email').send_keys(user_email)
    get_element('register_nickname').send_keys('24557279')
    get_element('register_password').send_keys('wx49841926')
    get_code_image('E:/test/imooc.png')
    text=code_online('E:/test/imooc.png')
    get_element('captcha_code').send_keys(text)
    get_element('register-btn').click()

run_main()