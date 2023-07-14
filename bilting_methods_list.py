''''# append (add element at the end of the index in list)
l1=[1,2,3,4,5]
l1.append('python')
print(l1)
l1.append([1,2,4])
print(l1)
#extend  (add element as sepret index at the end of list)
l1.extend([4,5,6,7])
print(l1)

#insert() insert an element of satisfaid position
l1.insert(3,'program')
print(l1)

#write ato find sum of all list element
l=[1,2,3,4]
print(sum(l))'''

#write to find sum of all list without using builting fun
l1=[1,2,3,4,5]
count=0
for i in l1:
     count+=i
print(count)


#count() it calculat totle ocurance of given element of list
l2=['python','python123',1,3,55,'python']
print(l2.count('python'))

# len()  display total length of list element
print(len(l2))
#min()
l=['java','c','python']
print(min(l))

#max()
print(max(l))

#ord() it display ascii charcter
# capitle ch diffrent ascii no and smoll ch diffrent ascii no
print(ord('c'))  #99
print(ord('A'))  #65
print(ord('a'))  #97

#chr()  it display ascii no ch
print(chr(99))

# write a program take a two list and add list elements sum to new_list
a=[1,2,3]
b=[3,2,4]
new_list=[]
for i in range(0,3):
     new_list.append(a[i]+b[i])
print(new_list)

#pop()
l1=[1,2,3,4,5]
print(l1.pop(2)) # pass index value to delete element
print(l1.pop())# if don

# del()  #it delete element of list
del(l1)#it delet all list
l1=[5,6,7,8]
del(l1[1])  #delete element of 1st list and you do not inser without index value
print(l1)

#remove()
l1=['python',2,3,'java']  # if you remove sum element or string than you string name not index no
l1.remove('python')
print(l1)

#reverse ()
l1.reverse()
print(l1)

#sort()  it same as order by -- asending order
l=[10,20,30,40,50,5.3,3]
l.sort()
print(l)

