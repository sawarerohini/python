# string function
#write a python program to check string capitalize or not
x=input("enter your string:")
cap=x.capitalize()
if x== cap:
    print("yes capitalize")
else:
    print("not capitalize")

# count()  how many ch you chose ch how many times
s='python programing'
print(s.count('p'))

print(s.count('o',5))# check o ch count at start from position 5

#count how many times prasent in l
l = "we learn python programing lang python is simple python123 python"
print(l.count('python'))

#find()  --position (index)
l = "we learn python programing lang python is simple python123 python"
print(l.find('python'))
print(l.find('python',10,25))  # 10 begin index and 25 is ending index
print(l.find('thame'))  #if thise string not prasent than display -1

#len()
s='suvidha'
print(len(s))

# write a python program to find the no of characters present in string without using len function
count=0
for i in 'suvidha parmar':
    count+=1
print(count)

#
p='we learn python programing lang python is simple python123 python'
print(p.find('python'))
if  (p.find('python')):
    print('is present')
else:
    print('not present')

# index()  find and index both are same but only diffrence is if string are not present than display error
a='Akshika'
print(l.index('A'))


#isalpha()
a='Akshika123'
print(a.isalpha())
print(a.isalnum())

#islower()
print(a.islower())

# isupper()
print(a.isupper())

# isdegit()
print('123'.isdegit)

#upper()
print('suvidha'.upper())

#lower()
print('suvidha'.lower) # it convert in lowercase

#title()
print('saware rohini'.title()) #it convert each word first leter capital

# split()
s='hello word'
print(s.split())

print('today we learn python'.split())






