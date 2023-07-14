# function
def print_name():
    #print("hello")
    return "how are you"
#print_name()  colling function print_num
#print(print_num())
# addition of two no using function
def add_num(a,b):    #requried argument
    return a+b
print("adition of two num:",add_num(10,5))
print(add_num(20,30))

# take number from user
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
print("addition of",num1,num2,"is:",add_num(num1,num2))

# keyword argument
def display_details(id,name):
    print(id,name)

display_details(101,'suvidha')
display_details(name='suvidha',id=102)

# default function    if by defoult you not pass some argument than he give by defoult value
def print_add(name,loction='pune'):
    print(name,loction)
print_add('rani','latur')
print_add('suvidha')

# veriable length argument(non keyword argument)
#symbol (*n)
def percentag(sum1,sum2,sum3):
    avg = (sum1 + sum2 +sum3) /3
    print('average' , avg)

percentag (56, 61, 89)

def var_arg(*args):     # it pass tuple
    totle= 0
    for i in args:
        totle=totle+i
    avg =totle/len(args)
    print(avg)

var_arg(1,2,3,4,5,67,9)

# kwargs (keyword length arguments)  (**kwargs)
# symbol(**kwargs)
def emp_details(**kwargs):
    for k,v in kwargs.items():
        print("employees {} is {}".format(k,v))

emp_details(name='suvidha',add='pune')
print('*'*10)
emp_details(name="puja",add="latur",salary=30000,ph_no=273548192)








