'''import pdb
i =1
pdb.set_trace();
while i<=10:
    print(i)
    i+=1
'''
import pdb
def add(x,y):
    z = x+y
    return (z)

pdb.set_trace()
a=10
b=20
r =add(a,b)
print(r)
