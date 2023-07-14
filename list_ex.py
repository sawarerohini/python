'''# list
#symbol[]
l1=['abc','pqr',1,2,3,4,45]
print(type(l1))
print(l1)

# accessing list element
print()

l2=l1[2:]
#mutable
print(l1)
l1[1]='56'
print(l1)
l1[2:6] = [6,7,8,9]
print(l1)
#multiple value replace and add
#replace even position no
l1= [0,1,2,3,4,5,6,7,8]     #replace even position number with character [a,b,c,d,e]
print(l1[0:2])
l1[0::2] = ['a','b','c','d','e']
print(l1)'''

#list add
l1=[0,1,2,3,4,5]
l2=[6,7,8,9]
print(l1+l2)

#maltiplication
print(l1*2)

for i in [12,13,14,15]:
    print(i,end=" ")
