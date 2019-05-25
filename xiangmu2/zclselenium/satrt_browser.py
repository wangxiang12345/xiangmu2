#coding=utf-8
from selenium import webdriver
import time
import random
#生成随机用户名
from PIL import Image
#裁剪图片
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from ShowapiRequest import ShowapiRequest
driver = webdriver.Chrome()
#driver2 = webdriver.Firefox()
#driver1 = webdriver.Edge()
driver.get("http://www.5itest.cn/register")
driver.maximize_window()
time.sleep(5)
#print(EC.title_contains("注册"))
email_element = driver.find_element_by_id("register_email")
email_element.send_keys('sdfsd')
driver.find_element_by_id('captcha_code')
driver.save_screenshot('E:/test/imooc.png')
code_element=driver.find_element_by_id('getcode_num')
print(code_element.location)
left=code_element.location['x']
top=code_element.location['y']
length=code_element.size['width']+left
height=code_element.size['height']+top
im=Image.open('E:/test/imooc.png')
img=im.crop((left,top,length,height))
img.save("E:/test/imooc1.png")

r = ShowapiRequest("http://route.showapi.com/184-1","94740","89a85a49bc6c4507b0d24c7e83096ef8" )
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addFilePara("image","E:/test/imooc1.png") #文件上传时设置
res = r.post()
text=res.json()['showapi_res_body']['Result']
print(text) # 返回信息
