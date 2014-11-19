'''
List类型
    类字符串，是序列式数据类型，支持下标和切片操作
    列表可包含不同类型的对象，不像数组仅能容纳同一种类型元素；
    支持操作：pop/empt/sort/reverse
    dir(list) ：可得到可支持的所有方法
'''
alist=[123,"abc",'shao',['a','b','c']];
#print(alist); #输出list
#print(alist[2]);#访问：下标0起 ->shao
#更新
alist[2]='ling';
#print(alist[2]);
#追加元素到list
#alist.append('appendItem');
alist.pop(2); #删除并返回
#print(alist)

#删除：索引-del,值-remove
# del alist[0]; 
# alist.remove('ling');
# print(alist)

#切片 []  [:]  0 -1
#in、not int
alist=['a','b']
# print('a' in alist)
# print('2' in alist)
# print('b' not in alist)

#'+'  ,连接符，list合并
# '*' 重复操作符
alist=[8,-2,5];
for i in range(8):
    if(i%2==0):
        print(i)

#内建函数cmp:比较
#函数 len/max/min/sum/sorted/reversed
alist.sort();
alist.reverse();

#list/tuple函数可接受可迭代对象作为参数
#append、count、extend、index、insert、pop、remove、reverse()、sort、
#sort、extend、reverse无返回值，在列表内操作

'''
List 嵌套
'''
M=[
   [1,2,3],
   [4,55,6]
]
for m in M:
    print(m)
print(M[1][1]);    
#==================== List Comprehensions ,就像内置的map/filter函数
col2=[row[1] for row in M] #获取第2列数据  List comprehensions
print(col2)
col2=[row[1]+3  for row in M] #获取第2列数据  List comprehensions
col2=[row[1]+3  for row in M if row[1]%2==0] #获取第2列数据  List comprehensions
print(col2)
#对角线上的值
coordinate=[M[i][i] for i in [0,1]];

#重复字符
double=[c*2 for c in 'spam'];

#List comprehension also work on any type that is a sequence in Python.

g=(sum(row) for row in M);#Create a generator of row sums
print("--》",next(g)) # 第一行
print(list(map(sum,M))) #map同样的功能：Map sum over items in M
#py3.0 :comprehension syntax can also be used to create sets and dictionaries
M=[
   [1,2,3],
   [4,5,6]
]
iset={sum(row) for row in M};
iDict={i:sum(M[i]) for i in range(2)};

iDict={x:ord(x) for x in 'spam'};















