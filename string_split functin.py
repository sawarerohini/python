#split()
s = 'hello world'
print(s.split())
print('today we,learn python'.split(','))

str = "hello#python#programming#we#learn#"
print(str.split('#',3))

#replace()
print(str.replace('python','java'))  # java replace python

#join()
name=['python','programming','we']
print('-'.join(name))

new_str='-'.join(name)
print(new_str)
print(type(new_str))

# write a program to find no of vowels present in enter string
n=input("enter your string:")
count = 0
for ch in n:
    if ch in 'AEIOUariou':
        count+=1
print(count)

# if ch=='a'or ch=='A' or ch=='E'
str=input("enter your string:")
count==0
for ch in str:
    if ch=='a'or ch=='A'or ch=='E':
        count+=1
print(count)

print(n)

