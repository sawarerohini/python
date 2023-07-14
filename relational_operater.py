# write a program to find the enter no is even or odd
num=4
if num % 2==0:
    print(" no is even");
else:
    print("no is odd");

 #write a program take a day no fron user (1 to 7) 1 monday 2tusday 3wensday
day=int(input("enter day number between (1-7):"))
if day==1:
    print("today is monday");
elif day==2:
    print("today is tuesday");
elif day==3:
    print("today is wensday");
elif day==4:
    print("today is thersday");
elif day==5:
    print("today is friday");
elif day==6:
    print("today is saterday");
elif day==7:
    print("today is sunday");
else:
    print("invalid day")

#take name from user and also check charcter from user and check char is prasent in or not
name='mohini'
x='m'
if x in name:
    print("yes prasent")
else:
    print("not")
#your strin or not
name='abc'
z='abc'
if z in name:
    print("it is string")
else:
    print("not string")
#write a program to find the enter char is vowel or not
vowel='AEIOUaeiou'
ch= input("enter character:")
if ch in vowel:
    print(ch,"is vowel")
else:
    print(ch,"is not")
#write a program to find gretest number between 3 no (20,30,50)
#if male ,age
gender =input("enter your gender like F or M:")
age= int(input("enter your age:"))
height = int(input("enter your hight:"))
if gender=='M':
    if age > 30 and height > 168:
        print("he is eligible")
    else:
        print("not eligible")
elif gender=='f':
    if age > 25 and height > 155:
        print("she is eligible")
    else:
        print("not eligible")
else:
    print("both are not eligible")



