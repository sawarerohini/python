# write a program to find a charecter present in string or not if present in which index it is present and how many time it is present
string=input("enter a string")
ch=input("enter ch to check:")
if ch in string:
    print(string.index(ch))
    print(string.count(ch))

# write a python function to check whether a number falls in a given range
def numrange(number):
    r=range(0,50)
    if number in r:
        print("yes",number,"falls in",r)
    else:
        print("no",number,"not fall in",r)
a= int(input("enter a number:"))
numrange(a)

d=dict()
for i in range(0,4):
    for j in range(i):
        d[i] = j
print(d)




