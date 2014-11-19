'''
Map:k-v
'''
D={'k1':'v1',"k2":'v2'}
#按k取值
print(D['k2']);
#更新k值
D['k2']='new Value'

#增加key
D={}
D['name']='shaoling'

#嵌套可以是任何类型：Map、list、set
rec={'name':{'first':'shao','last':'ling'},'job':'dev'}

#List []    set/map {}

#Sorting Keys: for Loops
#key无序的，放入和取出的顺序可能不一致
keys=list(D.keys()) #unordered keys list
keys.sort()   #sorted keys list
for k in keys:
    print('k:',D[k])
    
#上边需3步操作，一步操作
for key in sorted(D):
    print(key,":",D[key])

squares=[x ** 2 for x in [1,2,3,4]];#平方
print(squares)
squares=[]
for x in [1,2,3,4]:
    squares.append(x);
    
#simplicity and readability first   :简单和可阅读性第一，其次是性能
#性能测试：time/timeit/profile 模块

#若key不存在，取值则报错，需判断存在再取值

print('f' in D)    

if not 'f' in D:
    print("missing key=f")

v=D.get('f',0)  #若不存在，返回默认值







