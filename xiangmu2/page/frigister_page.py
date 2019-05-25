#coding=utf-8
from xiangmu2.zclselenium.find_element import  FindElement
class Frigister_Page(object):
    def __init__(self,driver):
         self.fdelement=FindElement(driver)
    def get_email_element(self):
        return self.fdelement.get_element("user_email")
    def get_email_element_error(self):
        return self.fdelement.get_element('user_email_error')
    def get_user_name_element(self):
        return self.fdelement.get_element('user_name')
    def get_user_name_element_error(self):
        return self.fdelement.get_element('user_name_error')
    def get_password_element(self):
        return self.fdelement.get_element('password')
    def get_password_element_error(self):
        return self.fdelement.get_element('password_error')
    def get_code_element(self):
        return self.fdelement.get_element('code_text')
    def get_code_element_error(self):
        return self.fdelement.get_element('code_text_error')
    def get_button_element(self):
        return self.fdelement.get_element('register_button')
