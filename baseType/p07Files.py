'''
'''
#f=open('data.txt','w') #当前目录下，创建文件,默认是读'r'
#size=f.write("helloworld\n")
#print("写入长度：",size)
#f.close()
f=open('data.txt') #默认模式是读r
text=f.read()
print("文件内容是：",text)
f.close();
#dir(f)
#help(f.seek)

#
data=open('data.bin','rb')#打开二进制文件
print(data[4:8])



