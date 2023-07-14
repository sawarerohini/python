# if n is odd,print weird
n= int(input("enter your no:"))
# n= list(n)
# print(type(n))
if n%2 ==1:
    print("weird")
elif  n<2 and n>5:
    print("not weird")
elif n<6 and n>20:
    print("weird")
else:
    print("not weird")

#creat  a code reading intiger value less than n .for all non negative intigers lessthan n,print square of enter intiger value
# ex: the list of non negative intiger that are less than 3 . print the square of each no in a separate line
n= [0,1,2,2,3,5]
for i in n:
    print(i)
square =[]
for i in n:
    square.append(i * i)
    print("the square of ",i, "is", square)

#










