from selenium import webdriver
from xiangmu2.zclselenium.find_element import FindElement
from  xiangmu2.page.register_page1 import RegisterPage
from xiangmu2.handle.frist_handle import LoginHandle
import time
from xiangmu2.page.frigister_page import Frigister_Page
driver=webdriver.Chrome()
driver.get('http://www.5itest.cn/register')
# frist=LoginHandle(driver)
# frist.send_user_email('5545')

# f=FindElement(driver)
# f.get_element('user_email').send_keys('5565665')

# j=Frigister_Page(driver)
# j.get_button_element().click
# k=RegisterPage(driver)
# k.get_email_element().send_keys('5546')
# R=Fristr_Biseness(driver)
# R.scuess_button()
time.sleep(10)
h=LoginHandle(driver)
text=h.get_user_text('emaill_error','请输入有效的电子邮件地址')
print(text)