'''
urllib库提供了一个从指定的URL地址获取网页数据，然后对其进行分析处理，获取想要的数据
参考：http://www.nowamagic.net/academy/detail/1302859

'''
import urllib.parse;
import urllib.request;
url='http://www.baidu.com/';
header = { 'User-Agent' :  'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }
#没有data则为get,否则为post
#若post需编码
data={'name':'shaoling'}
#urllib.parse.urlencode(data).encode();#默认UTF编码
#req=urllib.request.Request(url,data,headers=header) #post
req=urllib.request.Request(url,headers=header)
response=urllib.request.urlopen(req);
#page=response.read();
print(response.info()) #获取响应头
print('code:',response.getcode());
print('url:',response.geturl());

#看返回对象有什么方法
print(dir(response))
print("==========================")
#print(help(response.read()))
#print(dir(response.read()))

#看帮助
#help(urllib.request.urlopen);
#参考官方urllib模块，返回类文件对象
#read() , readline() , readlines()，fileno()和close()与文件对象完全一样
#info()：返回一个httplib.HTTPMessage 对象，表示远程服务器返回的头信息。
#getcode()：返回Http状态码，如果是http请求，200表示请求成功完成;404表示网址未找到。
#geturl()：返回请求的url地址。

#将远程数据下载到本地。
urllib.request.urlretrieve(url);



