#coding=utf-8
import logging
import os
import datetime
class UserLog:
    def __init__(self):
        #控制台输入日志
        # consle=logging.StreamHandler()
        # logger.addHandler(consle)
        #文件输出日志
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        base_dir=os.path.dirname(os.path.abspath(__file__))
        log_dir=os.path.join(base_dir,'logs')
        log_file=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")+'.log'
        log_name=log_dir+'/'+log_file

        #创建一个流
        self.file_handle=logging.FileHandler(log_name)
        #日志级别
        self.file_handle.setLevel(logging.INFO)
        #格式化
        self.formatter=logging.Formatter('%(asctime)s ,  %(filename)s  , %(funcName)s , %(levelno)s,%(levelname)s,%(message)s  ')
        #引入格式
        self.file_handle.setFormatter(self.formatter)
        #添加流
        self.logger.addHandler(self.file_handle)

    def get_log(self):
        return self.logger

    def log_close(self):
        self.logger.removeHandler(self.formatter)
        self.file_handle.close()
