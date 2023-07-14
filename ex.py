#Q1)A company decided to give bonus of 5% to employee if his/her year of service is more than 5 yrs.Ask user
# to give salary and year of service and print the net bonus amount
salary=eval(input("enter your salary:"))
year_survice=eval(input("enter year of survice:"))
if year_survice>5:
    print("years salary(+bonus)=",salary+(salary)*5/100)
else:
    print("your not eligible for bonus")

# no of positive no and no of negative no
list=[10,34,55,-23,6,-23,-1,45,-35,-2]
po_count ,neg_count=0 ,0
for num in list:
    if num>=0:
        po_count+=1
    else:
        neg_count +=1
print("positive number in list:",po_count)
print("negative number in list:",neg_count)

# no of even no and no of odd
list=[10,34,55,-23,6,-23,-1,45,-35,-2]
count_odd=0
count_even=0
for x in list:
    if not x%2:
        count_even+=1
    else:
        count_odd+=1
print("no of even no:",count_even)
print("no of odd no:",count_odd)

# find no of zero in list
list=[10,34,55,-23,6,-23,0,45,-35,-2]
count=0
for i in list:
    if i==0:
        count+=1
        print("no of zero in list is:",count)


# create a class student using multiple object display student ditails
class student:
    def __init__(self,id,name,course,address):
        self.id = id
        self.name = name
        self.course = course
        self.address = address
    def student_details(self):
        print("id:",self.id,"name:",self.name,"course:",self.course,"address:",self.address)
s1=student(2,'rohi','software_testing','latur')
s2=student(3,'kajal','mine','pune')
s1.student_details()
s2.student_details()

# create employee details
class employee:
    def __init__(self,name,salary,address):
        self.name=name
        self.salary=salary
        self.address=address
    def employee_details(self):
        print("name:",self.name,"salary:",self.salary,"address:",self.address)
e1=employee('rohini',34000,'pune')
e2=employee("sahana",4599,"mumbai")
e3=employee("anurag",43500,"haidrabad")
e1.employee_details()
e2.employee_details()
e3.employee_details()

# non paramiterized constractor
class student:
    def __init__(self):
        print("non-paramiterized constrctor")
    def show(self,name):
        print("hello",name)
s1=student()
s1.show("friend")

# parameterized constructor
class student:
    def __init__(self,name):
        print("parametrized constructor")
        self.name=name
    def show(self):
        print("hello",self.name)
s1=student("friend")
s1.show()

# inheritance one parent class and one child class
class student:
    def student_details(self):
        name="raj"
        print("student name:",name)
class school(student):
    def school_details(self):
        schoolname="MDM"
        print("school name:",schoolname)
d=school()
d.student_details()
d.school_details()

class employee:
    def employee_details(self):
        name="rohini"
        print("employee name:",name)
class company(employee):
    def company_details(self):
        company="TATA"
        print("company name:",company)
o=employee()
o=company()
o.employee_details()
o.company_details()

# multilavel inheritance
class grandparent:
    def grandparent_details(self):
        grandparent_name = 'keshav'
        yej=90
        print("grandparent_name:",grandparent_name,"yej:",90)
class parent(grandparent):
    def parent_details(self):
        parent_name='dnyanoba'
        yej=50
        print("parent name:,parent yej:",parent_name,yej)
class chaild(parent):
    def chaild_details(self):
        chaild_name='rohini'
        yej=21
        print("chaild name:",'yej:',chaild_name,yej)
g=parent()
g=chaild()
g.grandparent_details()
g.parent_details()
g.chaild_details()

# multiple inheritance
#multiple parent class and one chaild class
class addition:
    def add(self,a,b):
        print("addition of two no:",a+b)
class substraction:
    def sub(self,c,d):
        print("substraction of two no:",c-d)
class multiplication:
    def multi(self,e,f):
        print("multiplication of two no:",e*f)
class division:
    def divi(self,g,h):
        print("division of two no:",g/h)
class chaild(addition,substraction,multiplication,division):
    pass
m=chaild()
m.add(20,31)
m.sub(42,53)
m.multi(45,54)
m.divi(453,56)

# polymorphism
#same method name same parameter but diffrent implimentation
class calculator:
    num1=23
    num2=45
    def calculation(self):
        print("will calculate")
class addition(calculator):
    def calculation(self):
        print(self.num1+self.num2)
class substraction(calculator):
    def calculation(self):
        print(self.num1-self.num2)
class multiplication(calculator):
    def calculation(self):
        print(self.num1*self.num2)
a1=addition()
s1=substraction()
m1=multiplication()

a1.calculation()
s1.calculation()
m1.calculation()



