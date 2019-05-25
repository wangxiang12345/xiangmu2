#coding=utf-8
from xiangmu2.handle.frist_handle import LoginHandle
import sys
sys.path.append('D:\\Program Files\\JetBrains\\pycharm\\ThreeNode\\xiangmu2\\biseniss')
class Fristr_Biseness(object):
    def __init__(self,driver):
        self.rigster_h = LoginHandle(driver)

    def user_bese(self,email,user_name,password,file_name):
        self.rigster_h.send_user_email(email)
        self.rigster_h.send_user_name(user_name)
        self.rigster_h.send_user_password(password)
        self.rigster_h.send_user_code(file_name)
        self.rigster_h.click_frigster_button()


    def first_button_error(self,email,user_name,password,file_name,assert_error,error_text):
        self.user_bese(email,user_name,password,file_name)
        if self.rigster_h.get_user_text(assert_error,error_text)==None:
            #print('email检测不成功')
            return True
        else:
            return False



    def login_email_error(self,email,user_name,password,file_name):
        self.user_bese(email,user_name,password,file_name)
        if self.rigster_h.get_user_text('emaill_error','请输入有效的电子邮件地址')==None:
            print('email检测不成功')
            return True
        else:
            return False
    def login_user_name_error(self,email,user_name,password,file_name):
        self.user_bese(email, user_name, password, file_name)
        if self.rigster_h.get_user_text('user_name_error','字符长度必须大于等于4，一个中文字算2个字符')==None:
            print('用户名检测不成功')
            return True
        else:
            return False
    def login_password_error(self, email, user_name, password, file_name):
        self.user_bese(email,user_name, password, file_name)
        if self.rigster_h.get_user_text('password_error','最少需要输入 5 个字符')==None:
            print('密码格式检测不成功')
            return True
        else:
            return False
    def login_code_error(self, email, user_name, password, file_name):
        self.user_bese(email, user_name, password, file_name)
        if self.rigster_h.get_user_text('code_error','验证码错误')==None:
            print('验证码检验不成功')
            return True
        else:
            return False
    def scuess_button(self):
        if self.rigster_h.get_register_text()==None:
            return True
        else:
            return False




