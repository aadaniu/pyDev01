class Worker:
    def _init_(self,name,pay):
        self.name=name
        self.pay=pay
    def lastName(self):
        return self.name.split()[-1] #Split string on blanks
    def giveRaise(self,percent):
        self.pay*=(1.0+percent)
