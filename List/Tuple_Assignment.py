#write the program to print the same of integer values present in list
l1=[1,2,3,4]
print(sum(l1))
#write a program to find enter name is present in list of employee name or not
name=input("enter your name:")
list=["rani","radha","akash"]
if name in list:
  print("yes present")
else:
  print("not present")
# write a program that accepts a list from user and print the alternet element of list
new_list=[]
l=int(input("how many element you want to enter:"))
print(type(l))
#l=list(l)
print(type(l))
print("enter",l,"element")
for i in range(l):
    data=int(input())
    new_list.append(data)
print(new_list)
print('alternat element are:')
for i in range(0,len(new_list),2):
   print(new_list[i])
#4.Write a program tht accepts a list from user. Your program should reverse the content
# of list and display it. Do not use reverse() method.
l=eval(input("enter list element:"))
print(type(l))
l= list(l)
print(type(l))
for i in l:
     l[-1:len(l):]
print(l)

#6Find  and  display  the  largest  number  of  a  list  without  using  built-in  function  max().
# Your program should ask the user to input values in list from keyboard.
list1=eval(input("enter list number:"))
print(type(list1))
list1=list(list1)
print(type(list1))
max=0
for i in list1:
    if(i>max):
     max=i
print("the largest number of list",max)

#7.Write a program that rotates the element of a list so that the element at the first index
# moves to  the  second  index,  the  element  in  the  second  index  moves  to  the  third  index,  etc.,
#and  the element in the last index moves to the first index.
l1=eval(input("enter list number:"))
l1=list(l1)
print("orignal list number")
print(l1)
l1=l1[-1:] + l1[:-1]
print("rotaete list")
print(l1)

# 8.Write a program that input a string and ask user to delete a given word from a string.
text=input("enter your string:")
words=text.split(' ')
data=input("enter a word to delete:")
status = False
for word in words:
    if word == data:
        words.remove(word)
        status = True
if status:

    text= ' '.join(words)
    print("string after delation",text)
else:
     print("word is not in string.")

#---diff
"""s=input("inter your string:")
u=input("enter word to delete:")
l1=s.split(' ')
print(l1)
l1.remove(u)
print("after removing ",(l1))
s=' '.join(l1)
print(s)
"""

# 9.Write  a  program  with  a function  that  accepts a  string from  keyboard  and  create  a  new  string after
# converting  character  of each  word  capitalized.  For  instance,
# if the  sentence  is  "stop  and smell the roses." the output should be "Stop And Smell The Roses"
s=input("enter a sentence:")
print(s.title())










