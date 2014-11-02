'''
Created on 2014年11月2日

@author: shaoling@shaolingweb.cn
'''
import redis;
r=redis.StrictRedis(host='192.168.1.111');
r.sadd('set-key','a','b','c');
r.srem('set-key','c','d');
r.scard('set-key');
r.smembers('set-key');
r.smove('set-key', 'set-key2','a');

r.sdiff('skey1','skey2');
r.sinter('skey1','skey2');
r.sunion('skey1','skey2');
