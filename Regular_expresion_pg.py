# regular Expresion
import re
lang = 'we learn python programing python'
# findall() # return a list that contain all the macth of patern in the string
k = re.findall('python',lang)
print(k)

# search()  thise methoed return the match object if there is a match found in a string it return posion
s= re.search('python',lang)
print(s.span())  # first occurance posion no
print(s.group())

# sub()  ---replace
# if you chang python to java
x = re.sub('python','java',lang)
print(x)

# split
l= "th-is is p-ython pro-gramming"
m ='today we learmn python'
y= re.split('-',l)
x = re.split(' ',m)
print(x)
print(y)

data = "tufasdgdf"
reg = "[fag]"         # match f a or g from data any where ...
# if you check password than use thise re.search method "[@A3]"
# re.search
if re.search(reg,data):
    print("match pattern")
else:
    print('not')

# re.match
if re.match(reg,data):      #match any ch if starting of string
    print("match")
else:
    print("not")

# how to creat pattern
password = "Rohini@123"
reg = "[A-Z][a-z]*[@][0-9]*"
if re.search(reg,password):
    print("correct password")
else:
    print("not correct password")

