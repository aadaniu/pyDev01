'''
读Excel
http://pypi.python.org/pypi/xlrd模块
http://www.cnblogs.com/lhj588/archive/2012/01/06/2314181.html
'''
import xlrd,sys,xdrlib
data =xlrd.open_workbook("d:/sku.xls");
table = data.sheets()[0];
#table = data.sheet_by_name(u'Sheet1')#通过名称获取
#row=table.row_values(i) #获取整行(数组)
#table.col_values(i)
# 获取行数和列数
#nrows = table.nrows
#ncols = table.ncols
# for i in range(nrows ):
#     print( table.row_values(i));

 

    