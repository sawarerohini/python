#1. Write a python program using class which contains two variables of type integer. Create and
#initialize the object using parameterized constructor. Write a method to display maximum
#from given two numbers for all objects
class twonumbers:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def display_maximum(self):
      if self.num1>self.num2:
        print("maximum no is:",self.num1)
      else:
        print("maximum no is:",self.num2)

m1 = twonumbers(30,50)
m1.display_maximum()

#2. Write a program to perform all the arithmetic operations between two numbers
class Calculater:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        print("addition",self.num1+self.num2)
    def substract(self):
        print("sbtraction",self.num1-self.num2)
    def multi(self):
        print("multiplication",self.num1*self.num2)
    def division(self):
        print("division",self.num1/self.num2)
    def modulus(self):
        print("modulus",self.num1%self.num2)
    def floor_division(self):
        print("floor_division",self.num1//self.num2)
    def exponent(self):
        print("exponent",self.num1**self.num2)
c1=Calculater(34,78)
c1.add()
c1.substract()
c1.multi()
c1.division()
c1.modulus()
c1.exponent()
c1.floor_division()

#3. Write a program to find the records of students having greater marks.
class student:
    def __init__(self,name):
        self.name=name
        self.marks = []
    def add_marks(self,score):
        self.marks.append(score)
    def greatest_marks(self):
        return max(self.marks),self.name

s=student('alex')
s.add_marks(94)
s.add_marks(45)
s.add_marks(67)

s1=student("alex")
s2=student("mahi")
s1.add_marks(67)
s1.add_marks(90)

s2.add_marks(78)
s2.add_marks(65)

highest_marks = max(s1.greatest_marks(),s2.greatest_marks())
print('highest_marks is:',highest_marks)
