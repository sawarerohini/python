rows =5
for i in range(1, rows+ 1):
    for j in range(1,i+1):
        print('*',end=' ')
    print(' ')
#1)
'''
*  
**
***
****
*****'''
#2)
'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15'''

rows =5
a =1
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(a,end =' ')
        a+=1
    print(' ')

#3) revers
'''
11111
2222
333
44
5'''
row = 5
b =0
for i in range(rows,0,-1):
    b+=1
    for j in range(1,i+1):
        print(b,end=' ')
    print(' ')

#4)
row = 5
x = 65
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(chr(x),end =' ')
        x +=1
    print(' ')

# 5)
rows =8
a=1
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print(' ')
#6)
''' 1 2 3 4 5
 6 7 8 9 
 10 11 12
 13 14 
 15
'''
rows=5
c=1
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(c,end=' ')
        c+=1
    print(' ')

# print first line 4 '*' and second line 9 and threed
row=3
for i in range(row+1,1):
    for j in range(1,i+1):
        print('#',end=' ')
    print()

n=4
for i in range(n):
    for j in range(n-i-1):
        print(" ",end='')
    for j in range(i+1):
        print("#",end=" ")
    print()

