d={}
# bank details
bank={'name':'sbi','city':'pune','address':'tapkir chok'}
print(bank)
# employees detail dectionary
employees={'name':'rahul','ph_no':'5379267553','salary':'34000'}
print(bank)
#car details dic
d={}   # symbol of dictionary
car={'brand':'hundai','color':'red','modele':'abc','year':2022,'year':2002}#it update year:2023 to 2002 becouse dictionary deos not allow duplicat value
print(car)
print(type(car))

# how to access keys from dictionary
print(car['brand'])
#changing elements
car['brand']='pqrt'
print(car)

# you can not pass list as key in dictionary
# you can pass tuple becouse tuple is immutable

# length of car
#len()
print(len(car))

# zip() it function use to pair
# thise function is first value consider key and second value it retan object
# zip() (1,'python',2,'rani')
l1=[1,2,3]
l2=['python','java','.net']
#dict() convert in to dictonary
# o/p d1={1:'python',2:'java',3:'.net'}
d1=dict(zip(l1,l2))
print(d1)



