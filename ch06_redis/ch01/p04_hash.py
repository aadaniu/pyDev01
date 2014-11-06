'''
Created on 2014年11月2日

@author: shaoling@shaolingweb.cn
'''
import redis;
r=redis.StrictRedis(host='192.168.1.111');
r.hmset('hash-key', {'k1':'v1','k2':'v2'});
r.hmget('hash-key',['k1','k2']);
r.hlen('hash-key');
r.hdel('hash-key','k2');



