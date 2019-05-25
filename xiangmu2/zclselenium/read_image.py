#coding=utf-8
from PIL import Image
import pytesseract
import requests
from ShowapiRequest import ShowapiRequest
# image=Image.open('E:/test/test1.jpg')
# text=pytesseract.image_to_string(image)
# print(text)

r = ShowapiRequest("http://route.showapi.com/184-1","94740","89a85a49bc6c4507b0d24c7e83096ef8" )
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addFilePara("image","E:/test/imooc1.png") #文件上传时设置
res = r.post()
text=res.json()['showapi_res_body']['Result']
print(text) # 返回信息