#set symbol {}
#it is immuteble detatype
#it remove the duplicat element
#it is unorder
#you do not pass index value and also do not use slicing
#set() it convert one detatype into set
#set()
l1=[1,3,2,4,4,5,6]
s1=set(l1)
print(s1)
print(type(s1))

days={'monday','tuesday','thursday','wednesday','thursday'}
print(days)
days2={'firday','monday','tuesday','thursday','saturday','sunday'}

#create empty set using set()
s2={} #it display type dictionary becouse dictionary simbol also like{}
s3=set() #empty set created
print(type(s3))

#add single element in set
days.add('sunday')
print(days)
#multiple element add in set
days2.update(['wendsday','saturday','monday'])
days2.update([2,3])
print(days2)

#remove element using discard()
days.discard('suvidha')
print(days)
#days.remove('suvidha')
print(days)

#clear  all deta remove set is empty
#days.clear()
#print(days)

print(dir(days))

