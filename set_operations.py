s1={'a','b','c','d','e','f'}
s2={'h','i','j','k','a','b','c'}
s3={1,2,3}
s4=s3.copy() #copy s3 element to new set s4
print("copied set",s4)

# union (combain two set and display unique value)
print(s1|s2)
print(s1.union(s2))
print(s1)
print(s2)

#intersection  display the common value in the two set
print(s1.intersection(s2))
# & it work same intersect
print(s1&s2)

#difference it  use toshow s1 -s2
#uncommon element of those set
#it give priority on s1 set
print(s1.difference(s2))
#it give priority on s2 set
print(s2.difference(s1))

#symetric_difference()
print(s1.symmetric_difference(s2)) #display uncommon deta to both set

#intersection_update
# add common vales and remove uncommon deta
s1.intersection_update(s2)
s1^s2
print(s1)

#pop()  it delite element , you do not write index value in pop becouse it is unorder
s1.pop()
print(s1)

print(s1.issubset(s2)) #ask the s1 is present in s2  o/p true
print(s1.issuperset(s2)) #ask s1 is supperset of s2   o/p false

#we can remove multiple element
# than use symmetric_diffrence
s1={1,2,3,4,5,6,7,8,9}
s2=[5,6,3,8]
s1.symmetric_difference_update(s2)
print("after removing [5,6,3,8] s1 is:",s1)