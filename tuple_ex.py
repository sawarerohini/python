'''#tuple()
t=()            #tuple write in()
t1=("python",)
print(t1)#single element in tuple
#t1[1]='c'  # item assignment can not possible in tuple
#slicing
t=(1,2,3,45)
print(t[1:])

#del()
a=(1,2,3,4,4)
del(a)
print(a)

# concatination
t1=(1,2,3,45,67)
t2=(4,'c','python',2,4)
print(t1*3)
print(t1+t2)

#tuple multiply to 2
for i in t1:
    print(i*2)
# take tuple element from user and print alternet element
for i in range(0,len(t1),2):
    print(t1[i])

# write a python program to take tuple element from user and find squr of all tuple element
tupl=eval(input("enter tuple element"))
print(tuple)
print(type(tuple))
for i in tupl:
    print(i**2)

# min() and max()
#print min of t1 and print max of t1
print(min(t1))
print(max(t1))'''
# convert tuple into list
list1=[1,2,3,'c',4,'python']
#tuple()
x=tuple(list1)
print(type(x))
print(x)

# builting function in tuple
#count()
print(x.count(2))   #it display element how many times

#index()
print(x.index('python'))     #it display element index position
