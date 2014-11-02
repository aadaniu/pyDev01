'''
Created on 2014年11月2日

@author: shaoling@shaolingweb.cn
'''
import redis;
r=redis.StrictRedis(host='192.168.1.111');
r.rpush('mylist', 'last');
r.lpush('mylist','first');
r.rpush('mylist','new last');
r.lrange('mylist',0,-1);
r.lpop('mylist');
r.ltrim('mylist', 0, -1);
