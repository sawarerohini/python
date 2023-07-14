# creat class : data (attribute) ,method(functionality)
# attributes : name,roll no marks
# method : display marks, display details
#syntax:
'''class Student:
    pass
class Student(object):
'''
class Student:
    def __init__(self):  #constructer defoult constracter
        print("i am constracter")
        # self :parameter which is used to refer method of object
s1= Student() # s1 is object  # call calss
#self is assign the value to object
class Student1:
    def __init__(self,roll_no,name,marks):    #parameterized constracter # atributes
        print("Iam constracter")
        self.rollno =roll_no
        self.name =name
        self.mark =marks
    def show(self):
        print(self.name,self.rollno,self.mark) # ('suvidha',10,28)

s1=Student1(10,'suvidha',28)
s2=Student1(11,'rohi',89)
s1.show()
s2.show()

# 1) create a class to maintane book_details  display details
#(book_id,book_name,price
class books:
    def __init__(self,book_id,book_name,price):
        self.book_id = book_id
        self.book_name = book_name
        self.book_price = price
    def show(self):
        print(self.book_id,self.book_name,self.book_price)

b1=books(1,"core_python",5000)
b2=books(2,"selenium",800)
b1.show()
b2.show()

# creat a class culculater initialize two numbers parameters and calculat addition ,substraction of two number using one object
# if you want to differnt diffrent values for diffrent diffrent operation
class calculator:
    def __init__(self,num1,num2,num3,num4,num5,num6,num7,num8,num9,num10,num11,num12,num13,num14):
        self.num1= num1
        self.num2= num2
        self.num3= num3
        self.num4 = num4
        self.num5 = num5
        self.num6 = num6
        self.num7 = num7
        self.num8 = num8
        self.num9 = num9
        self.num10 = num10
        self.num11 = num11
        self.num12 = num12
        self.num13 = num13
        self.num14= num14
    def add(self):  #method defaine
        print("addition",self.num1+self.num2)
    def subtract(self):
        print("substraction",self.num3-self.num4)
    def multi(self):
        print("multiplication",self.num5*self.num6)
    def division(self):
        print("division",self.num7/self.num8)
    def floordivision(self):
        print("floordivision",self.num9//self.num10)
    def mod(self):
        print("modulus",self.num11%self.num12)
    def exponent(self):
        print("exponent",self.num13**self.num14)
c1=calculator(1,2,3,4,5,6,7,8,9,10,32,54,654,24)
c1.add()
c1.subtract()
c1.multi()
c1.division()
c1.floordivision()
c1.mod()
c1.exponent()



 #create object c1 of class calculator
  #method
