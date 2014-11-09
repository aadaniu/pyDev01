'''
读Excel
http://pypi.python.org/pypi/xlrd模块
http://www.cnblogs.com/lhj588/archive/2012/01/06/2314181.html
'''
import xlrd
#post请求
import urllib
import sys
data =xlrd.open_workbook("d:/sku.xls");
table = data.sheets()[0];
#table = data.sheet_by_name(u'Sheet1')#通过名称获取
#row=table.row_values(i) #获取整行(数组)
#table.col_values(i)
# 获取行数和列数
nrows = table.nrows
#ncols = table.ncols
def login(): 
    url="http://ko.erp.xx.com/shaoling/login.action"
    data={
            "loginName":'',
            "loginPwd":''
            }
    postData=urllib.parse.urlencode(data);
    postData=postData.encode();#默认UTF8
    #cookie=http.cookiejar.CookieJar();#保存cookie,为登录后访问
    res=urllib.request.urlopen(url, postData);#关闭close :res.close();
    print("登录结果：",res.status,res.reason);
    if res.status==200:
        url="http://ko.erp.xx.com/shaoling/put.action"
        for rowNum in range(nrows ):
            if rowNum>1:
                row=table.row_values(rowNum);
                if row:
                    skuId=str(int(row[0]))
                    startDate=xlrd.xldate.xldate_as_datetime(row[1], 0)
                    endDate=xlrd.xldate.xldate_as_datetime(row[2], 0)
                    data={
                          'skuId':skuId,
                          'startTime':startDate,
                          'endTime':endDate
                          }
                    data=urllib.parse.urlencode(data);
                    res=urllib.request.urlopen(url, data.encode());
                    rep="第"+str(rowNum-1)+"条："+skuId +'\t' +str(startDate) +"\t" +str(endDate);
                    if res.status == 200:
                        rep+="  ---->成功"
                        print(res.read())
                    else:
                        rep+="  ---->失败"   
                    #print(rep)    
login();    