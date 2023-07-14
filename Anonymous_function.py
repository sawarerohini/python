from functools import reduce
# Anonymous function / lambda function
#syntax:
# lambda argument: expression
x= lambda a: a+2    #x is veriabal use to stor lambda value
print(x(10))

addition =lambda a,b : a+b
print(addition(10,20))

#find greter number
greater = lambda a,b : a if a>b else b
print(greater(40,49))

# square
square = lambda a: a**2
print(square(9))


# builting function of lambda
# filter()  it is used to filterout data from list object.
#use filter function to find even no .
l1=[1,2,3,4,5,6,7,8,9]
f=list(filter(lambda a: a%2 ==0,l1))
print(f)

# find odd no
l2=[1,2,3,4,5,6,7,8,9]
d=list(filter(lambda a: a%2 ==1,l2))
print(d)

#map()
# if you want to apply same operation or condition to all list's element
#then you use map fuction
m=list(map(lambda a:a**2,l1))
print("sqaur of all element:",m)

# reduce()   sum of list element
#we will reduce condition(expretion) reduce in single value(element) or result.
r= reduce(lambda a,b :a+b,l1)
print("sum of list element:",r)
