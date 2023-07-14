# decorator: it is a function is change functionality of anather functoin
# it is a function that accept function as parameter and return a function
# takes the result of function,modify the result and return not it
#
def div(a,b):
    print(a/b)  # a greter ,b lesser
print("simple functoin calling")
div(4,2)
div(4,2)
div(2,4)

def smart_div(func): #func = div function pass as parameter
    def inner(a,b):
        if a <b :
            a,b =b,a
        return inner

div= smart_div(div)
div(2,4)

def decor(fun):
    def inner():
        a=fun()
        add =a+5
        return add
    return inner()
@decor
def num():
    return 10
print(num())


