'''#1.Write a program to print your  entered name in reverse order
n=input("enter your name:")
print (n[::-1])
#2.write a program to print every thered charcter of enter string
sentance=input("enter your string")
print(sentance[::3])
#3.write a python program to find the no of charcter prasent in string without using len()
string=input("enter your string")
count=0
for i in string:
    count+=1
print(count)
#4.write a python program to print the no of vowels present in enter string
string=input("enter your string:")
count=0
for i in string:
    if i in 'AEIOUaeiou':
        count+=1
print(count)'''
#5.write a program to find a charcter present in string or not?if present in wich index it is present .
# and how many times it is present
string="python program"
print("o" in string)
ch="o"
print(string.find(ch))
print(string.count(ch))












