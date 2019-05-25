#coding=utf-8
import sys
sys.path.append(r'D:\Program Files\JetBrains\pycharm\ThreeNode\xiangmu2\case')
from xiangmu2.util.excel_util import ExcelUtil
from  xiangmu2.keywordselenium.actionMethod import ActionMethod

class KeyWordCase:
    def run_main(self):
        self.actionmethod=ActionMethod()
        excelutil = ExcelUtil(r'D:\Program Files\JetBrains\pycharm\ThreeNode\xiangmu2\config\keyword.xls')
        handle_lins=excelutil.get_lines()
        print(handle_lins)
        if handle_lins:
            for i in range(1,handle_lins):
                is_run=excelutil.get_col_value(i,3)
                print(is_run)
                if is_run=='yes':
                    method =excelutil.get_col_value(i,4)
                    send_value=excelutil.get_col_value(i,5)
                    handle_value=excelutil.get_col_value(i,6)
                    except_result_method=excelutil.get_col_value(i,7)
                    except_result=excelutil.get_col_value(i,8)
                    print(method,send_value,handle_value)
                    self.run_method(method,send_value,handle_value)
                    if except_result!='':
                        except_value=self.getexcept_result_value(except_result)
                        print(except_value)
                        if except_value[0]=='text':
                            print(except_result_method)
                            result=self.run_method(except_result_method)
                            print(result)
                            if except_value[1] in result:
                                excelutil.write_value(i,'pass')
                            else:
                                excelutil.write_value(i, 'fail')
                        elif except_value[0]=='element':

                            result=self.run_method(except_result_method,except_value[1])
                            print('-----',result)
                            if result:
                                excelutil.write_value(i,'pass')
                            else:
                                excelutil.write_value(i, 'fail')


    #获取预期结果值
    def getexcept_result_value(self,data):
        return data.split('=')

    def run_method(self,method,send_value='',handle_value=''):
        method_value=getattr(self.actionmethod, method)
        if send_value !='' and handle_value!='':
            result=method_value(send_value,handle_value)
        elif send_value=='' and handle_value !='':
            result=method_value(handle_value)
        elif send_value!='' and handle_value=='':
            result=method_value=(send_value)
        elif send_value=='' and handle_value=='':
            result=method_value()
        return result
if __name__ == '__main__':
    test=KeyWordCase()
    test.run_main()