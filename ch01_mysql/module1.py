class FirstClass:
    def setData(self,value):
        self.data=value
    def display(self):
        print(self.data)
class SecondClass(FirstClass):
    def display(self):
        print('Current value="%s"'%self.data)
x=SecondClass()
x.setData("shaoling")
x.display()    
print("==============ClassThird================")
class ThirdClass(SecondClass):
    def __init__(self,value):#是两个下划线
        self.data=value
    def __add__(self,other):# +
        return ThirdClass(self.data+other)
    def __str__(self):#print()
        return '[ThirdClass:%s]'%self.data
    def mul(self,other):
        self.data*=other
t=ThirdClass('abc')
t.display()
print(t)
t=t+"def" #__add__
t.display()
