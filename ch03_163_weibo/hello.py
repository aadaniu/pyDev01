'''
Python模拟163登陆获取邮件列表
参考：http://developer.51cto.com/art/201205/338269.htm

cookielib — Cookie handling for HTTP clients¶
        https://docs.python.org/2/library/cookielib.html
        The cookielib module has been renamed to http.cookiejar in Python 3.
urllib2 — extensible library for opening URLs¶
        https://docs.python.org/2.7/library/urllib2.html 
        The urllib2 module has been split across several modules in Python 3 named urllib.request and urllib.error.
Created on 2014年7月12日
@author: sl
'''
headers ={"User-agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}  


 
import http.cookiejar
import urllib 
import urllib.error 
import urllib.parse
import urllib.request 

import xml.etree.ElementTree as etree  # xml解析类  


class Login163:
    #伪装浏览器
    header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    username = '' 
    passwd = '' 
    cookie = None #cookie对象  
    cookiefile = './cookies.dat' #cookie临时存放地  
    user = '' 
    def __init__(self,username,passwd):  
        self.username = username  
        self.passwd = passwd  
        #cookie设置  
        self.cookie = http.cookiejar.LWPCookieJar() 
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cookie))  
        urllib.request.install_opener(opener)  
    #登陆      
    def login(self):         
        #请求参数设置  
        postdata = {  
            'username':self.username,  
            'password':self.passwd,  
            'type':1 
            }  
        postdata = urllib.parse.urlencode(postdata)  
 
        #发起请求  
        req = urllib.request.Request(  
                url='http://reg.163.com/logins.jsp?type=1&product=mail163&url=http://entry.mail.163.com/coremail/fcg/ntesdoor2?lightweight%3D1%26verifycookie%3D1%26language%3D-1%26style%3D1',  
                data= postdata,#请求数据  
                headers = self.header #请求头  
            )  
 
        result = urllib.request.urlopen(req).read()  
        result = str(result)  
        self.user = self.username.split('@')[0]  
 
        self.cookie.save(self.cookiefile)#保存cookie  
          
        if '登录成功，正在跳转...' in result:  
            #print("%s 你已成功登陆163邮箱。---------\n" %(user))  
            flag = True 
        else:  
            flag = '%s 登陆163邮箱失败。'%(self.user)  
             
        return flag  
 
   #获取通讯录  
    def address_list(self):  
        #获取认证sid  
        auth = urllib.request.Request(  
                url='http://entry.mail.163.com/coremail/fcg/ntesdoor2?username='+self.user+'&lightweight=1&verifycookie=1&language=-1&style=1',  
                headers = self.header  
            )  
        auth = urllib.request.urlopen(auth).read()  
        for i,sid in enumerate(self.cookie):#enumerate()用于同时返数字索引与数值，实际上是一个元组:((0,test[0]),(1,test[1]).......)这有点像php里的foreach 语句的作用  
            sid = str(sid)  
            if 'sid' in sid:  
                sid = sid.split()[1].split('=')[1]  
                break 
        self.cookie.save(self.cookiefile)  
          
        #请求地址  
        url = 'http://twebmail.mail.163.com/js4/s?sid='+sid+'&func=global:sequential&showAd=false&userType=browser&uid='+self.username  
        #参数设定(var 变量是必需要的,不然就只能看到:<code>S_OK</code><messages/>这类信息)  
        #这里参数也是在firebug下查看的。  
        postdata = {  
            'func':'global:sequential',  
            'showAd':'false',  
            'sid':sid,  
            'uid':self.username,  
            'userType':'browser',  
            'var':'<?xml version="1.0"?><object><array name="items"><object><string name="func">pab:searchContacts</string><object name="var"><array name="order"><object><string name="field">FN</string><boolean name="desc">false</boolean><boolean name="ignoreCase">true</boolean></object></array></object></object><object><string name="func">pab:getAllGroups</string></object></array></object>' 
            }  
        postdata = urllib.parse.urlencode(postdata)  
          
        #组装请求  
        req = urllib.request.Request(  
            url = url,  
            data = postdata,  
            headers = self.header  
            )  
        res = urllib.request.urlopen(req).read()  
          
        #解析XML，转换成json  
        #说明：由于这样请求后163给出的是xml格式的数据，  
        #为了返回的数据能方便使用最好是转为JSON  
        json = []  
        tree = etree.fromstring(res)  
        obj = None 
        for child in tree:  
            if child.tag == 'array':  
                obj = child              
                break 
        #这里多参考一下，etree元素的方法属性等，包括attrib,text,tag,getchildren()等  
        obj = obj[0].getchildren().pop()  
        for child in obj:  
            for x in child:  
                attr = x.attrib  
                if attr['name']== 'EMAIL;PREF':  
                    value = {'email':x.text}  
                    json.append(value)  
        return json  
          
#Demo  
print("Requesting......\n\n")  
login = Login163('xxxx@163.com','xxxxx')  
flag = login.login()  
if type(flag) is bool:  
    print("Successful landing,Resolved contacts......\n\n")  
    res = login.address_list()  
    for x in res:  
        print(x['email'])  
else:  
    print(flag) 




















