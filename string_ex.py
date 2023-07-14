# string : sequence of character
a = "python programing"
print(a[2:])    # thon programing
# [] slice operator [start_index:stop_index:reverse_index]
# print your string in revers
print(a[ : :-1])

# wap a py pro to take one string from user and print that string in revers order
s= input("enter your name:")
print("revers name is:",s[ : :-1])
# print learn
# substring
a='we learn python'
print(a[3:8])
# print oht
print(a[-2:-5:-1])
# print in revers neael ew
print(a[-8::-1]) #(-1 should be write in revers order)
# write a python program to check enter string is palindrom or not like(naman,madam)
b=input("enter your string")
str = b[::-1]
if b==str:
    print("thise is palindron")
else:
    print("thise is not polindron")




