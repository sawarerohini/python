#1. Write a program to find greater number between two entered numbers.
a=5
b=8
if a>b:
    print("'a' is greter no:")
else:
    print("'b' is greter no:")
#write a program to find enter no are equal or not
a=5
b=5
if a==b:
    print("enter no is equal")
else:
    print("enter no is not equal")
#write a program to find enter no is positive or negative
num=int(input("enter no :"))
if num>0:
    print("enter no is positive")
else:
    print("enter no is negative")
#write a program to find enter no is even or odd
n=int(input("enter no:"))
if n % 2==0:
    print("enter no is even")
else:
    print("enter no is odd")
#write a program to find enter charcter is vowel or not
vowel='AEIOUaeiou'
ch=input("enter charcter:")
if ch in vowel:
    print(ch,"is vowel")
else:
    print(ch,"is not vowel")
#write a program to print the days of week according to the enterd day number
day=int(input("enter day number between (1-7):"))
if day==1:
    print("today is monday");
elif day==2:
    print("today is tuesday");
elif day==3:
    print("today is wednesday");
elif day==4:
    print("today is thursday");
elif day==5:
    print("today is friday");
elif day==6:
    print("today is saturday");
elif day==7:
    print("today is sunday");
#write a program to performe arithmatic operations between two intigers value according to the operater enter by user
#addition
a=int(input("enter no 1:"))
b=int(input("enter no 2:"))
add=a+b
print("addition of a & b:",add)
#substraction
a=int(input("enter no 1:"))
b=int(input("enter no 2:"))
print("substractraction",a-b)
#multiplication
a=int(input("enter no 1:"))
b=int(input("enter no 2:"))
print("multiplication",a*b)
#division
a=int(input("enter no 1:"))
b=int(input("enter no 2:"))
print("division",a/b)
#floor division
a=int(input("enter no 1:"))
b=int(input("enter no 2:"))
print("floor division",a//b)
#exponential
a=int(input("enter no 1:"))
b=int(input("enter no 2:"))
print("exponential",a**b)

   # Logical operators
#1. Write a program to check entered character is vowel or not?
vowel='AEIOUaeiou'
ch=int(input("enter charcter:"))
if ch in vowel:
    print(ch, "is vowel")
else:
    print(ch,"is not vowel")
#2. Write a program to print weekday if entered day number is 1,2,3,4,5 and print weekend if entered day is 6 or 7.and invalid day if value not between 1 to 7
day=int(input("enter day number between(1-7)"))
if day==1:
    print("it is weekday")
elif day==2:
    print("it is weekday")
elif day==3:
    print("it is weekday")
elif day==4:
    print("it is weekday")
elif day==5:
    print("it is weekday")
elif day==(6 and 7):
    print("enter no day is weekend")
else:
    print("invalid day")
#write a program to find gretest amoung 3 number
a=2
b=5
c=1
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
else:
    print("c is greater")
#4. A candidate is recruited based on following criteria: If male, age should be above 30 yrs and height above 16
# 0. then he is eligible If female, age should be above 25yrs and height above 155. then she is eligible.
gender=input("enter your gender like 'male' or female':")
age=int(input("enter your age:"))
height=int(input("enter your height:"))
if gender=='m':
    if age > 30 and height > 168:
        print("he is eligible")
    else:
        print("not eligible")
elif gender=='f':
    if age>25 and height>155:
        print("she is eligible")
    else:
        print("not eligible")
else:
    print("both are not eligible")








