#while loop
# write to print 1 to 10 no
counter = 1 # we are initializing counter veriable
while counter <=10:
    print(counter)
    counter +=1 # counter = counter+1
print("done")
# write to print 10 to 1
counter =10
while counter >=1:
    print(counter)
    counter -=1
# write to print user name 5 times
name=input("enter your name:")
c=1
while c<=5:
    print(name)
    c+=1
#write a pro to enter name n no of times
name=input("enter your name:")
num=int(input("enter your num:"))
c=1
while c<=num:
    print(c,name)
    c+=1
#write a program to print the table of 5
table=5
while table<=50:
    print(table)
    table+=5
# dispay 5*1=1 table
c=1
x=5
while x<=50:
    print("5 *" ,c,'=',x)
    c+=1
    x+=5
# write a pro to print table of enter no
num=int(input("enter a no:"))
i=1
while i<=10:
    print(num,"*",i,"=",i*num)
    i+=1
# write a pro to print 5 to 15
counter=5
while counter <=15:
    print(counter)
    counter+=1
#write a pro  to print the values between two enter no
num1=1
num2=10
while num1<=num2:
    print(num1)
    num1+=1
num1=int(input("enter your no1:"))
num2=int(input("enter your no2:"))
while num2<=num1:
    print(num2)
    num2+=1






# write a pro to print even no between 1 to 10 even=2 4 6 8
a=1
while a<=10:
    if(a%2==0):
        print(a)
    a+=1