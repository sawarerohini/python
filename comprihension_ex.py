#list comprihension:
p = [x for x in range(1,11)]
print(p)
# [exp for item in iterable if conditional]
# [exp if conditional else stmt for item in iterable]
e =[x for x in range(1,11) if x%2 ==0]
print(e)
a =[x if x>2 else x+1 for x in range(1,11)]  # x if x>2 else x+1
print(a)

