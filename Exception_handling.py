# Exception handling
# Types of error
#logical error
#runtime error
#syntax error
# 4 keywords exception error
# if interpriter error not user understand than user use thise keyword block to give readable error
#block
# if try block condition is run than give else block massage otherwise exception massage
a = int(input("enter first no:"))
b = int(input("enter second no:"))
try:
    c=a/b
except Exception as e:
    print("please enter correct value")
else:
    print("answer is :",c)
finally:
    print("thank you of inserting value")


