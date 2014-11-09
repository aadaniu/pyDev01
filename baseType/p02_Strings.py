'''
'''
import re;#正则
s="shaoling"
print(s[-1]); #最后一个字符,0起
#分片
print(s[1:3]) #前包括，后不包括
print(s[:-1]) #除去最后一个
print(s*2);#重复输出2遍
print("hello "+s);#字符串连接

#字符串不可变
print(s.find('ling'));
s.replace('ao', 'AO');
s.split(',')
s.upper()
s.isalpha()
s.lstrip().rstrip().strip();
print('%s shao %s' %('hello','ling!')) #格式化

#获取帮助
#print(dir(s))
#print(help(s.replace));

ord('\n');

#正则  
# [  \t]* 零个或多个tab或空格
match=re.match('Hello[ \t]*(.*)world', 'Hello Python world')
print(match.group(1))
match = re.match('/(.*)/(.*)/(.*)', '/usr/home/lumberjack')
for x in match.groups():
    print("-->"+x)
    
