import xlrd
from xlutils.copy import copy
class ExcelUtil:
    def __init__(self,excel_path=None,index=None):
        if  excel_path==None:
            excel_path=r'D:\Program Files\JetBrains\pycharm\ThreeNode\xiangmu2\config\casedata.xls'
        if index==None:
            index=0
        self.excel_path=excel_path
        self.data=xlrd.open_workbook(self.excel_path)
        self.table=self.data.sheets()[index]
        self.rows =self.table.nrows
        #获取exclel数据
    def get_data(self):
        result=[]
        rows=self.get_lines()
        if rows !=None:
            for i in  range(self.get_lines()):
                col=self.table.row_values(i)
                result.append(col)
            return  result
        else:
            return False
    #获取excel有多少行
    def get_lines(self):
        rows=self.table.nrows
        if rows>=1:
            return rows
        else:
            return None
    #获取单元格的数据
    def get_col_value(self,row,cell):
        if row<=self.get_lines():
            data=self.table.cell(row,cell).value
            return data
        else:
            return  None
    #写入数据（需安装xlutils包）
    def write_value(self,row,value):
        read_value=xlrd.open_workbook(self.excel_path)
        write_data=copy(read_value)
        write_data.get_sheet(0).write(row,9,value)
        write_data.save(self.excel_path)
if __name__ == '__main__':
    ex=ExcelUtil(r'D:\Program Files\JetBrains\pycharm\ThreeNode\xiangmu2\config\keyword.xls')
    print(ex.get_col_value(4,4))




