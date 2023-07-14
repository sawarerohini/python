#1)	find no of characters, no  of words or number of lines in Python text file.
f1=open ('text.txt','r')
#print(len(f1.read()))
print(len(f1.read().split(' ')))
#print(len(f1.readlines()))
f1.close()
#2)	Write a program to Count the number of upper-case alphabets present in a text file “PYTHON.TXT”.
def upper_count ():
    upper=0
    f=open("PYTHON.TXT",'r')
    line=f.read()
    for i in line:
        if i.isupper() == True:
            upper+=1
    print("no of upper_case alphabets are present in file:",upper)
upper_count()

#3)	A text file “PYTHON.TXT” contains alphanumeric text. Write a program that reads this text file and writes
# to another file “PYTHON1.TXT”
#entire file except the numbers or digits in the file.
f2=open("PYTHON.TXT",'r')
f3=open("PYTHON1.TXT",'w')
rec = f2.read()
for a in rec:
    if a.isdigit() !=True:
        print(a,end=" ")
    f3.write(a)
f2.close()
f3.close()

#4)	Write a program to count the words “to” and “the” present in a text file “python.txt”.
f4=open("python.txt",'w')
f4.write("i am going to the college")
print('ok')
f4=open("python.txt",'r')
total=0
words= f4.read().split()
for a in words:
    if (a.islower() == "to" or a.islower() == "the"):
        total+=1
print("no of words:",total)
f4.close()

#5)	Write a program to display all the lines in a file “python.txt” along with line/record number.
f5=open("python.txt",'r')
count =0
lines = f5.readlines()
for a in lines:
    count+=1
print("no of lines are:",count)
f5.close()






