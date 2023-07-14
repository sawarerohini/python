# 1.Write a Python function to find the Max of three numbers.
# def max_num(num1,num2,num3):
#     return max(num1,num2,num3)
# num1 = int(input("enter num1:"))
# num2 = int(input("enter num2:"))
# num3 = int(input("enter num3:"))
# if num1>num2 or num1>num3:
#     print("num1 is max number")
# elif num2>num1 or num2>num3:
#     print("num2 is max number")
# else:
#     print("num3 is max number")

'''def maximum(a, b, c): 
   list = [a, b, c] 
   return max(list) 
# Driven code  
x = int(input("Enter First number"))
y = int(input("Enter Second number"))
z = int(input("Enter Third number"))
print("Maximum Number is ::>",maximum(x, y, z)) 
'''



# 2.Write a Python function to sum all the numbers in a list.
# def sum(numbers):
#     totle=0
#     for x in numbers:
#         totale += x
#     return totale
# print(sum((2,4,5,6)))
#
# 3.Write a Python function to multiply all the numbers in list.
# def multiplylist(mylist):
#     result=1
#     for i in mylist:
#         result = result * i
#     return mylist
# list1=[2,4,6,8,76,9]
# print(multiplylist(list1))






# 4.Write a Python program to reverse a string.
string="i am learing python"
print(string[::-1])

# 5.Write a Python function to check whether a number falls in a given range.
def test_range(n):
    if n in range(10,25):
        print(n,"thise number is falls in range")
    else:
        print("thise number not in range")
test_range(23)


