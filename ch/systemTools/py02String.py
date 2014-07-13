'''
String Method Basics
@author: sl
Created on 2014年7月13日
'''
mystr = 'xxxSPAMxxx'
print(mystr.find('SPAM')) # return first offset
print(mystr.replace('SPAM', 'aa')) # global replacement，returns a new string
print(mystr) #串的不变性
#a module called re that allows regular expression patterns
print('SPAM' in mystr )# substring search/test

mystr.strip() # remove whitespace
#rstrip() lstrip()
#lower()
#.isalpha() 字母
#isdigit()
import string
print(string.ascii_lowercase)
#print(string.whitespace)
#.join
#.split()
#.append('!')
int("42"), eval("42") # string to int conversions
str(42), repr(42) # int to string conversions
("%d" % 42), '{:d}'.format(42) # via formatting expression, method
"42" + str(1), int("42") + 1 # concatenation, addition
#the first expression triggers string concatenation
#the second invokes integer addition

'''
Python 3.X: Unicode and bytes
using str in text mode
    handles Unicode encodings and lineend conversions
bytes in binary mode
    transfers bytes to and from files    unchanged

'''






