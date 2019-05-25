#coding=utf-8
import ddt
import sys
import os
sys.path.append('D:\\Program Files\\JetBrains\\pycharm\\ThreeNode\\xiangmu2')
curPath = os.path.abspath(os.path.join(os.getcwd()))
sys.path.append(curPath)
from   xiangmu2.biseniss.rigisterbisiness import Fristr_Biseness
from   selenium import webdriver
import time
import unittest

import HTMLTestRunner
from xiangmu2.util.excel_util import ExcelUtil
from xiangmu2.log.user_log import UserLog

ex = ExcelUtil()
data =ex.get_data()
@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.file_name = 'E:/test/test6.png'
        cls.log=UserLog()
        cls.logger=cls.log.get_log()


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')

        self.case = Fristr_Biseness(self.driver)

    def tearDown(self):
        for mothod_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd(), '../report/', case_name + '.png')
                self.driver.save_screenshot(file_path)
        time.sleep(3)
        self.driver.close()
        #邮箱，用户名，密码，验证码，错误信息定位元素，错误提示信息
    # @ddt.data(['gfsdfgsf@163.com','335484','wxfsfdf','code','emaill_error','请输入有效的电子邮件地址'],
    #          ['111', '5656523', 'wxfsfdf', 'codex', 'emaill_error', '请输入有效的电子邮件地址'],
    #          ['.com', '562326', 'wxfsfdf', 'codex', 'emaill_error', '请输入有效的电子邮件地址']
    #          )
    # @ddt.unpack
    @ddt.data(*data)
    def test_first_button(self,data):
        email, user_name, password, file_name, assert_error, error_text=data
        email_error = self.case.first_button_error(email,user_name,password,file_name,assert_error,error_text)
        test=self.assertFalse(email_error, '注册失败')
        if test==False:
            self.logger.info(email,user_name,password,file_name,assert_error,error_text,test)
        else:
            self.logger.info(email, user_name, password, file_name, assert_error, error_text)
        # if email_error==True:
        #     print('邮箱格式错误注册成功，邮箱CASE检验失败')
if __name__ == '__main__':
    path=os.path.join(os.getcwd(),'xiangmu2/report/frist1.html')
    f=open(path,'wb')
    suite=unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='注册页面测试报告',verbosity=1,description='第一次测试报告')
    runner.run(suite)