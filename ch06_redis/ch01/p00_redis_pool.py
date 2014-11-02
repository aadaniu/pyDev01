'''
Created on 2014年11月2日
redis 池化，默认一个实例维护自己的连接池，可修改为多实例共享一个池，
@author: shaoling@shaolingweb.cn
'''
import redis;
pool=redis.ConnectionPool(host='192.168.1.111',port=6379);
r=redis.Redis(connection_pool=pool);
r.set('name','shaoling');
print(r.get('name'));

#redis pipeline机制，可以在一次请求中执行多个命令，避免多次的往返时延。
pipe=r.pipeline();
pipe.set('key1',11);
pipe.set('key2',11);
pipe.execute();
pipe.set('key3',3).set('key4',4).execute();