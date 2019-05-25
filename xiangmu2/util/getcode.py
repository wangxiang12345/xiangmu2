#coding=utf-8
from PIL import Image
from ShowapiRequest import ShowapiRequest
import time
class GetCode:
    def __init__(self,driver):
        self.driver=driver

    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_element_by_id('getcode_num')
        print(code_element.location)
        left = code_element.location['x']
        top = code_element.location['y']
        length = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left, top, length, height))
        img.save(file_name)
        time.sleep(3)

    # 解析图片获取验证码
    def code_online(self,file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-1", "94740", "89a85a49bc6c4507b0d24c7e83096ef8")
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addFilePara("image", file_name)  # 文件上传时设置
        res = r.post()
        text = res.json()['showapi_res_body']['Result']
        time.sleep(3)
        return text