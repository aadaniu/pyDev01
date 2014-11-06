import re;#正则
'''
python的字符串是不可变的。
文本处理：即文本格式转换。

'''
from pkg_resources import basestring

#让一行文本扩展到多行,使用续行符：\
s='Just a test\
还是上一行的内容，不是换行';
#print(s)
#让字符串的输出分两行，使用换行符：\n
s='第一行\n\
第二行';
#print(s)
#3个引号式的跨行，无需续行、换行符，按'原貌'存入：
s='''第一行
,第二行
''';
#print(s)
#也可以加r或R表示该字符串是‘原’字符，需要它的原貌
#r使得，转义字符也被忽略
s=r"""第一行
第二行
""";
#print(s)
#字符串是无法改变的，任何操作总是创建新的字符串
s='my string'
#print(s[0]) # 'm'
#print(s[-2]) # 'n'
#切片访问字符串的一部分
#print(s[1:4]) # 'y s'
#print(s[4:]) # 'string'
#切片，第三个参数做为步长
#print(s[1::2])# 'ysrn'
#print(s[4:-1:2])# 'ti'
#遍历字符串
#for c in s:
    #print(c)
#字符串转为list
li=list(s);
#print(li)

#字符串拼接,或join()
s1='shao'
s2=' ling'
s=s1+s2
#print(s)
# *重复
s='xo'*3
#print(s)  #xoxoxo
#print(s.isdigit()) #若不为空且字符都是数字
#print(s.count('xo')) #子串出现的次数
#print(s.upper())
s='''第一行
第二行'''
li=s.splitlines();
# for x in li:
#     print(x)
#re模块：正则
# Template格式化含有变量的字符串

#用list得到字符串的字符
li=list('shaoling')
# for x in li:
#     print(x)
#字符 和 字符值 之间转换
#print(ord('a'))   #97
#print(chr(97)) #a
#print(repr(chr(97))) #'a'  ,
#repr函数和str函数：将任意值转为字符串，
#前者返回官方字符串表示，对python友好，使用于eval；
#后者用户友好，多用于输出
 

#python中的map、filter、reduce

#判断对象是否是字符串
def isAsString(obj):
    return isinstance(obj, basestring)
#print(isAsString("shaoling"))    
#print(isAsString([2,3]))    

#字符串对齐：
s='shao';
# print(s.ljust(12,'0'))#默认空格
# print(s.center(12))
# print(s.rjust(12,'x'))
#去除字符串2端空格
s='  shao  ';
# print(s.lstrip())
# print(s.rstrip())
# print(s.strip())

#字符串中变量格式化：格式化操作符%
s='name:%s  ，age:%s' % ('shaoling',28) #无需对非字符串对象使用str转换，%隐含转换
print(s)

#P49










