'''
Created on 2014年11月2日

@author: shaoling@shaolingweb.cn
'''
import redis
conn=redis.StrictRedis(host='192.168.1.111');
conn.set('key', 22);
conn.get('key');
conn.incr('key');
conn.incr('key',15);
conn.decr('key', 12);
conn.incrbyfloat('key', 2.23);
#字符串操作
r=conn;
r.append('name', 'Just a test'); #字符串追加
r.getrange('name', 1, 3);#取子串
r.setrange('name', 3,'new value');#从offset处设置新子串

#setbit getbit bitcount bitop





