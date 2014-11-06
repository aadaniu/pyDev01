'''
Created on 2014年11月6日

@author: shaoling@shaolingweb.cn
'''
from redis._compat import xrange
import redis;
import time;
import threading;
conn=redis.StrictRedis(host='192.168.1.111');
def publisher(n):
    time.sleep(1);
    for i in xrange(n):
        conn.publish('channel',i);
        time.sleep(1);
def run_pubsub():
    threading.Thread(target=publisher,args=(3,)).start();
    pubsub=conn.pubsub();
    pubsub.subscribe(['channel']);
    count=0;
    for item in pubsub.listen():
        print( item)
        count+=1;
        if count==4:
            pubsub.unsubscribe();
        if count==5:
            break;
run_pubsub();