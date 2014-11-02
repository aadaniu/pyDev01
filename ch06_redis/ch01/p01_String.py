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
