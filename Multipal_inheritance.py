#multipel inheritance
class Addition :
    def add(self,a,b):
        print(a+b)
class Substraction :
    def sub(self,a,b):
        print(a-b)
class Multiplication:
    def multi(self,a,b):
        print(a*b)
class chaild(Addition,Substraction,Multiplication):
    pass

c1 = chaild()
c1.add(12,34)
c1.sub(23,54)
c1.multi(34,65)
#if need to user enter value
a= int(input("enter a:"))
b= int(input("enter b:"))
class Addition :
    def add(self,a,b):
        print(a+b)
class Substraction :
    def sub(self,a,b):
        print(a-b)
class Multiplication:
    def multi(self,a,b):
        print(a*b)
class chaild(Addition,Substraction,Multiplication):
    pass

c1 = chaild()
c1.add(a,b)
c1.sub(a,b)
c1.multi(a,b)
