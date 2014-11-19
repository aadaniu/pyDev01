'''
元组：序列-支持切片，类似list但不可变，圆括号，任意类型，任意嵌套
'''
T=(1,2,3,4)
print(len(T))
T=T+(5,6)
print(len(T))
#Indexing ,slicing
print(T.index(4 )) #指定值出现的位置：0起
print(T.count(4)) #指定值出现几次
#T[2]=2  不可以这样操作，不可变的

#支持多种类型
T=(1,2,[3,4],'test')
print(T)

#为什么使用tuple类型？类似list，但支持更少的操作
#并不经常用！利用其不可变性



