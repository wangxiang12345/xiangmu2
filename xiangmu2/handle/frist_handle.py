#coding=utf-8
from xiangmu2.page.frigister_page import Frigister_Page
import os
from xiangmu2.util.getcode import GetCode
class LoginHandle(object):
    def __init__(self,driver):
        self.driver=driver
        self.fd_page=Frigister_Page(self.driver)
    #输入email
    def send_user_email(self,email):
        self.fd_page.get_email_element().send_keys(email)
    #输入用户名
    def send_user_name(self,user_name):
        self.fd_page.get_user_name_element().send_keys(user_name)
    #输入密码
    def send_user_password(self,password):
        self.fd_page.get_password_element().send_keys(password)
    #输入验证码
    def send_user_code(self,file_name):
        # get_code_text=GetCode(self.driver)
        # code=get_code_text.code_online(file_name)
        self.fd_page.get_code_element().send_keys(file_name)
    #获取文字信息
    def get_user_text(self,info,user_info):
        try:
            if info=='emaill_error':
                text=self.fd_page.get_email_element_error().text
            elif info=='user_name_error':
                text=self.fd_page.get_user_name_element_error().text
            elif info=='password_error':
                text=self.fd_page.get_password_element_error().text
            elif info=='code_error':
                text=self.fd_page.get_code_element_error().text
        except:
            text=None
        return  text

    #点击注册
    def click_frigster_button(self):
        self.fd_page.get_button_element().click()
    def get_register_text(self):
        return self.fd_page.get_button_element().text



