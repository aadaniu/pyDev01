'''
Created on 2014年11月3日

@author: shaoling@shaolingweb.cn
'''
import redis;
r=redis.StrictRedis(host='192.168.1.111');
r.zadd('key',3,'a',2,'b',1,'c'); #先分数后元素
r.zcard('key');
r.zincrby('key', 'a', 2);#加分
r.zscore('key', 'c'); #取分
r.zrank('key', 'a'); #得排名
r.zcount('key', 3, 8); #分数范围内的元素个数
r.zrange('key', 0, -1, withscores=True);
r.zrem('key',3,'a');#删除


r.zadd('zset-1',1,'a',2,'b',3,'c');
r.zadd('zset-2',4,'b',1,'c',0,'d');
r.zinterstore('zset-i', ['zset-1','zset-2']);#交集放到zset-i
rtn=r.zrange('zset-i', 0, -1, withscores=True);
r.zunionstore('zset-u', ['zset-1','zset-2'], aggregate='min');#
rtn=r.zrange('zset-u', 0, -1, withscores=True); #

