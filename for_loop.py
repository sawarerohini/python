#print(range(50))
for i in range(50):
    print(i)
# wap a pro to print even no between1 to 20
for i in range(0,21,2):
    print(i)
# print odd no between 1 to 50
for i in range(1,51,2):
    print(i)
# wap a pro to table of 5 using for loop
for i in range(5,51,5):
    print(i)
# print enter no form user and print that no to table
num=int(input("enter no:"))
for i in range(1,11):
    print(i*num)
# 1+2+3+4+5+6+7+8+9+10=55
total=0
for i in range(1,11):
    total=total+i
print(total)
#wap a py pro to find factorial no
n=int(input("enter no:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
# wap a py program to find  enterrd no is prim or not(1,3,5,7,11)
n=int(input("enter your number"))
if n > 1:
    for i in range(2, int(n/2)+1):
        if (n % i) == 0:
            print(n, "number is not prim")
        break
    else:
        print(n, "number is prim")
# or
n=int(input("enter no:"))
for i in range(2,n):
    if n%i==0:
        print(i,end=" ")
        print(i,"is prim")
        break
else:
    print(i,"is not prim")












