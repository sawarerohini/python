# open function
# file_handling
# create a file if file already create than file open
#open(file_name.txt,mod(r/w/a))
#use of if keyworld
# w = if old file is present than and deta is in file than thise deta will remove and new deta is fill using 'w'
import os
f = open("text.txt",'w')
#write mod creat new file open file for writing if existing file is creat than thse file deta
#delet and new file ceate
print("done")
f.write("today we learn python\n")  #write line in new created file
f.write("python s very simpal launguage\n")
#f.close()  # it use to close containt we can not write lines after close
print("done")
file=open("python.txt",'w')
file.write("my name is ROHINI\n")
file.write("I am learn SOFTWARE TESTING")
file.write("suvidha mam teaching is very nice")
print("ok")

file=open("PYTHON1.TXT",'w')
file.write("my name is ROHINI\n")
file.write("I am learn SOFTWARE TESTING")
file.write("suvidha mam teaching is very nice")
print("ok")



# if you create on different location file
# also with keyword use to creat anyther location file
f= open('C:\\ROHINI\\demo.txt','w')
print('done')
# or thise way also use
with open('C:\\ROHINI\\demo1.txt','w') as f1:
     f1.writelines(["hello all \n","we all are here for python \n","today we learn python\n"])
    # f1.close()

# append () (a)
with open ('C:\\ROHINI\\demo1.txt','a')as f1:
    f1.write("python is interpriter language")
    print("ok")
#    f1.close()

# read (r)
# how to read file
f2= open ("text.txt",'r+')
print(f2.read())
with open('C:\\ROHINI\\demo.txt','a') as f2:
    f2.write("python is very simple language")
    print("ok")

# readline =single line read /readlines is convert into list than after loop iterate all contains use
print(f.read())      #all read deta  #it convert in to string
print(f.readlines())

'''l1= f2.readlines()  #display deta in list format
print(l1)
for i in l1:
    if python in l1:
        print("yes")
else:
    print("no")

print(f2.readlines())
'''
