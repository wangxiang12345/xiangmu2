#coding=utf-8
import configparser
class ReadIni():
    def __init__(self,file_name=None,node=None):
        if file_name==None:
            file_name=r'D:\Program Files\JetBrains\pycharm\ThreeNode\xiangmu2\config\LocalElement.ini'
        self.cf=self.load_ini(file_name)
        if node==None:
            self.node='RegisterElement'
        else:
            self.node=node
    def load_ini(self,file_name):
         cf=configparser.ConfigParser()
         cf.read(file_name)
         return cf
    def get_value(self,key,node=None,):
        data=self.cf.get(self.node,key)
        return data
if __name__ == '__main__':
    readini=ReadIni()
    print(readini.get_value('user_email'))


