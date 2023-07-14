# String:
# 1) display charecters from even position
'''word = "polymorphism"
for i in range(len(word)):
    if i % 2==1:
     print(word[i],end =' ')

#print(word[1: :2])
# 2)display charcters from odd positions
string ="r2o3h4i5n4i2s1a4h5a4n2a"
for i in range(len(string)):
    if i % 2==0:
        print(string[i],end =' ')

# 3)display length of string
given_string = "my name is rohini"
print(len(given_string))

# 4)display length of string without using len function
given_string = "my college name is MDM"
count = 0
for i in given_string:
    count+=1
print(count)

# 4)find second max no in list
l1 = [1,2,3,4,5,6,7,8,1,6,3]
l1.sort[1,2,3,4,5,7,8,1,6,3]
print(l1[-2])

#5) add a at end of length of string
string = "Avishkar"
print(string+'a')
# 6) write a program to accept a string from user and accept aneyther string and stor in veriable and check
# and find all occuranc of string stor in  check veriable
string1=input("enter your string:")
veriable ="rohini"
if veriable in string1:
    print("string stor in veriable are present in string")
else:
    print("not present")

# list:
# 1) display following menu
#accept data
#add at last position
l1 =[1,2,3,4,5]
l1.extend('6')
print(l1)
# add at given position
l2=[1,2,3,4,5]
l2.insert(3,'numbers')
print(l2)

#2. delete data by value
# display massage deleted successfully or not found
l3=['c++','java','python']
l3.remove('python')
print(l3)
if (1==1):
    print("deleted successfully")
else:
    print("not found")


# 3. delete data by possion
# delete last posion
l4=[1,3,4,'rohini','sonali']
l4.pop()
print(l4)
#delete given posion element
l4=[1,2,3,'avishkar','anurag']
l4.pop(3)
print(l4)

#4. sort
# acending
l5=[1,9,7,4,5,6]
l5.sort()
print(l5)

#desending
l5=[1,9,7,4,5,6]
l5.sort[1,9,7,4,5,6]
print(l5)

# 5.reverce
# print in sortend order
l1=[1,10,9,4,5]
l1.sort()
print(l1)
# print in reverce order
l1=[1,'c++','java',3,5]
l1.reverse()
print(l1)

# 6.display data
# normal:
l2=['rohini','mohini','pratiksha']
print(l2)
# numbered:
l2=[23,23,232,32,4]
print(l2)

# 7) creat a list of city by accepting value by user and accept location and stor in location arrey and display
#1 st city and 1 st location of second city and 2nd location
city=eval(input("enter list element of city:"))
location=eval(input("enter list element of location:"))
city=list(city)
print(type(city))
print(city[1],location[1])
print(city[2],location[2])

# 8)creat a list and exchange a values as index and index as values
list=[12,1,3,7,8,5,8]
list1=[]


# set assignment
# write a program to accept name to user and stor into a set
#display following menu
#1. print(delet element if exist otherwise it show error)
set ={'rohi','sahana'}
print(set)
delete=eval(input("enter element to delete:"))
str_set=str(delete)
def Remove(set):
    set.remove('delete')
print(set)
if delete in set:
    print("exist in set")
else:
    print("it show error")

# add a element
set1={2,4,3,21,'rohi'}
set1.add('sahana')
print(set1)
# create one more set
set1 ={1,2,3,56,'c++','java','python',20}
set2 ={'c++',3,5,6,7,1,'python'}
# union of two set
print(set1.union(set2))
# intersection of two set
print(set1.intersection(set2))
# diffrence of two set
print(set1.difference(set2))
# convert set in to frozenset
fnum=frozenset(set1)
print("frozen object is:",fnum)
# exit

# 9) perfome all 9 operation on given list and genret list of list
# accept a number from user and check last digit of number
# if it is 1 than add 1st index and if it is 0 than it add at list in 0th posion
# e.g it should lock as follows
# [[10,[51],[52],[],[],[],[],[57]]
# [[10,30,20,40],[11,32,41,31],[22,32,42].....]
#if user enter 15 than the result list should be [[10,30,20,40],[11,32,41,31],[22,32,42],[],[],[15]]


#10)  creat a list to stor string in a list in following maner list
#(dxz,axz,bat,rat,cat,pat,bbc,cbm,...]pat axz
# all list are same on second posion should be consecutive if user add sat at the resultant list will be
#[bat,rat,cat,sat,bbc,bbm,cbm,....]
# if user add pick than it should be added at [bat,rat,cat,sat,bbc,bbm,cbm,pick]
list=['bat','rat','sat','cat','bbc','bbm','cbm']
list.append('abc')
print(list)

# dictionary:
# write a program to accept name of person and vehical name as value
#ask user do you want to continue
dict={'rohi':'activa','sahana':'bulat','ranjana':'activa','asmita':'activa'}
u=input("do you want to continue:")
print(dict)


#display following menu
# 1. add new person and vehicle
dict1={'suvidha':'BMT'}
dict.update(dict1)
print(dict)
# 2. delete a key from dictionary
del(dict['sahana'])
print(dict)
# accept key from user
a=input("enter key:")
print(a)
# check wethere key exists
d={'pavan':2000,'rani':3500,'sapana':3400}
n=input("enter key value:")
if n in d:
    print("present:",n)
else:
    print(" not present")
# if exist show key and values to user
# confirm for deletion if user enters y
# than delete otherwise no
#del(d['a'])
# 3.modify value of key

# accept key from user
# if exist show key and value to user
b=input("enter key value:")
# check whethere key exists
if b in d:
    print(d)
else:
    print("not present")
print(dict.items())
# ask for new value
v=input("enter new value:")
# 4.search vehicle for given name
print(dict.get('rohi'))'''
# 5.search list of peaple name how has given vehicle

# 6.display all keys
dict2={'abc':2436,'pqr':43534,'mno':52452}
print("keys:",list(dict2.keys()))
# 7.display all values
print("values:",dict2.values())


# write a program to display following menu
# 1.add new city and trees commonly found in city
d={'kokan':''
# 2.display all cites and the list of trees for all cites
print(d.values())
# 3.display list of perticular city
# accept a list from user search city and if found display list of trees
# display massege not found
# 4.display cityes containing tree
# accept a tree name from user and display all cityes in which the tree is there
# 5.delete city-accept city from user and delete the city found
# prompt user before deletion
# 6.modify tree list
# accept city and trees tobe added in the city.if city exist add trees at the end otherwise add
# city and list
#7.exist




# write a program to display following menu
# 1.add new city and trees commonly found in city

# write a program to display following menu
# 1.add new city and trees commonly found in city

# 2.display all cites and the list of trees for all cites

# 3.display list of perticular city
# accept a list from user search city and if found display list of trees
# display massege not found
# 2.display all cites and the list of trees for all cites

# 3.display list of perticular city
# accept a list from user search city and if found display list of trees
# display massege not found


















