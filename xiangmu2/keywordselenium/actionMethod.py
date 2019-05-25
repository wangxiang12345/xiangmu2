#coding=utf-8
from selenium import webdriver
from xiangmu2.zclselenium.find_element import FindElement
import time
class ActionMethod:
    def open_browser(self,browser):
        if browser=='chrome':
            self.driver=webdriver.Chrome()
        elif browser=='firefox':
            self.driver=webdriver.Firefox()
        else:
            self.driver=webdriver.Edge()
        return self.driver
    def get_url(self,url):
        self.driver.get(url)
    def find_element(self,key):
        fd=FindElement(self.driver)
        element=fd.get_element(key)
        return element
    def element_send_keys(self,value,key):
        element=self.find_element(key)
        element.send_keys(value)
    def click_element(self,key):
        element=self.find_element(key)
        element.click
    def sleep_time(self):
        time.sleep(3)
    def get_title(self):
        title=self.driver.title
        return title

    def close_browser(self):
        self.driver.close()
if __name__ == '__main__':
    A=ActionMethod()
    A.open_browser('chrome')
    A.get_url('http://www.5itest.cn/register')


