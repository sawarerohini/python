# local/global veriable:
#outsaid the function write veriabal colled global veriabal
#insaid the fun write veriabal colled local veriabal
a=10  #global veriable
def print_num():
    a=20 # local veriabal
    print(a)

print("global veriabal:",a)
print_num()  #20
print(a)  #10
print(a+10)
# if you write insaid veriabal value is write in outsaid use (global_a)
def print_num():
    global a
    a=20
    print(a)
print(a)
print_num()
print(a)
