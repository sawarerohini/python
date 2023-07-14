# write a read file and check how many uppercase alphabet are present in your file.(is.upper() 'python')
a = "Python PoGraMing"
upper = 0
for i in a:
    if i.isupper() == True:
        upper +=1
print(upper)

# find total lenth of ch in text.txt file without using length function
f1= open('text.txt','r')
a= f1.read()  # convert in string
#leanth= len(a)
count =0
for i in a:
    count +=1
print("total count ch :",count)
