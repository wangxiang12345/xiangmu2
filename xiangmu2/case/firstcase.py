#codoing=utf-8
import sys
import os
sys.path.append('D:\\Program Files\\JetBrains\\pycharm\\ThreeNode\\xiangmu2\\case')
curPath = os.path.abspath(os.path.join(os.getcwd()))
sys.path.append(curPath)
from   xiangmu2.biseniss.rigisterbisiness import Fristr_Biseness
from   selenium import webdriver
import time
import unittest

import HTMLTestRunner
from xiangmu2.log.user_log import UserLog


class FristCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.file_name='E:/test/test6.png'
        cls.log = UserLog()

        cls.logger = cls.log.get_log()

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.case=Fristr_Biseness(self.driver)
        self.logger.info('this is chrome')
        self.log.log_close()
    def tearDown(self):
        for mothod_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd(),'../report/',case_name+'.png')
                self.driver.save_screenshot(file_path)

        time.sleep(2)
        self.driver.close()
    def test_login_eimal_error(self):

        email_error=self.case.login_email_error('222gfsdfgsf@163.com','24455','wxfsfdf',self.file_name)
        test=self.assertFalse(email_error,'邮箱格式错误注册成功，邮箱CASE检验失败')
        self.logger.info(self.file_name,test)
        # if email_error==True:
        #     print('邮箱格式错误注册成功，邮箱CASE检验失败')

    def test_login_username_error(self):
        user_name_error=self.case.login_user_name_error('222gfsdfgsf@163.com', 'ddd', '12345ad', self.file_name)
        self.assertFalse(user_name_error, '用户名错误注册成功，用户名检验CASE失败')
        # if user_name_error==True:
        #     print('用户名错误注册成功，用户名检验CASE失败')
    def test_login_password_error(self):
        password_error=self.case.login_password_error('333gfsdfgsf@163.com', 'dddff', '123d', self.file_name)
        self.assertFalse(password_error, '密码格式输入错误注册成功，密码检测CASE失败')
        # if password_error==True:
        #     print('密码格式输入错误注册成功，密码检测CASE失败')
    def test_login_code_error(self):
        code_error=self.case.login_code_error('444fsfdgadg@163.com', 'dddf', '12345a', self.file_name)
        self.assertFalse(code_error, '验证码输入错误，注册成功')
        # if code_error==True:
        #     print('验证码输入错误，注册成功')
    def test_login_sucess(self):
        self.case.user_bese('555fsfasff@163.com', 'dddf', '12345ad', self.file_name)
        scuess=self.case.scuess_button()
        self.assertFalse(scuess,'注册失败')

        #     print('注册成功，CASE执行成功')
        # else:
        #     print('注册失败')
# def main():
#         frist = FristCase()
#         frist.test_login_eimal_error()
#         frist.test_login_code_error()
#         frist.test_login_username_error()
#         frist.test_login_password_error()
#         frist.test_login_sucess()

if __name__ == '__main__':
   # unittest.main()
    case_path=os.path.join(os.getcwd(),'xiangmu2/report/first_case.html')
    f=open(case_path,mode='wb')
    suite=unittest.TestSuite()
    suite.addTest(FristCase('test_login_sucess'))
    suite.addTest(FristCase('test_login_eimal_error'))
    suite.addTest(FristCase('test_login_username_error'))
    suite.addTest(FristCase('test_login_password_error'))
    suite.addTest(FristCase('test_login_code_error'))
    runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='注册页面测试报告0',verbosity=2,description='第一次测试报告')
    runner.run(suite)

