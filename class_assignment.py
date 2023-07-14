'''# 1. write a program to calculate length of file or number of line in the reals
f=(open('text.txt','r'))
print(len(f.readlines()))
# 2.find which line in file line is longest word
def wordFinder():
    with open('text.txt', "r") as f:
        words = f.read().split() # split() returns a list with the words in the file
        longestWord = max(words, key = len)# key = len returns the word size
        print(longestWord) # prints the longest word'''

#''' 3. calculat number of lines except new lines
f=(open('text.txt','r'))
print(f.readlines())

# 4. calculat number of occures each word in the reals
count=0
f=open('python.txt','r')
a=f.read()
for i in a:
    if a == 'p':
        count+=1
        print(f.readline())


# 5. calculat number and occures each charecter in string
'''# 6. find max no in a list
l1=[1,6,3,7,58,75]
print(max(l1))
# 7.find second max number in a list
l2=[1,4,3,6,78]
print(sorted(l2))
print(len(l2))
print(l2[1])
# 8.find two strings are antonyms of each other
# 9.find where the string antonym
# 10.revers word of input string
string=input("enter your string")
print(string[::-1])
# 11.chang first letter of each string in to capital
string="my name is rohini"
print(string.title())
# 12.find where string start with sam input char and end with sam input char
char=input("enter your char:")
char2=input("enter your end char:")
string1="python"
print(string1.find(char))
# 13.split a string into two words without using split function
string2="suvidha mam teaching very nice"
print(string2.strip('suvidha'))
print(string2.rstrip('mam'))
# 14.calculate length of string without using length function
string="programming"
count=0
for i in string:
    count+=1
print(count)'''

test_str = "Geeks"
# printing original string
print("The original string is : " + str(test_str))
# get all possible substrings
res = ([test_str[i:j] for i in range(len(test_str)) for j in range(i + 1, len(test_str) + 1)])

# sort substrings by length and alphabetically
res = [test_str[i:j] for i in range(len(test_str))
       for j in range(i+1,len(test_str)+1)]

# printing result
print("All substrings of string are : " + str(res))


# 16.input will be start index end index

string ="my name is rohini and my favourite language is python"
print("the original string is:" + str(string))
check_list=["rohini","favourite","language"]
res=dict()
for element in check_list:
    if element in string:
        strt =string.index(element)
        res[element]=[strt,strt + len(element)-1]
print("required extracted index:"+str(res))

# 17.input is list of string create new sentance using thise list.
l1=["rohan","omkar","harshali","indira","neha","indrajit"]

for string in l1:
    sentance = string.join(l1)
print(sentance)

#print(l1.split(','))
# 18.strip a string if a has any white space on both side without using strip function
string=" india is my country "
temp=""
for i in range(len(string)):
    if string[i] ==' ':
        continue
    temp = string[i+1:]
print(temp)


# 19.write a program to print start index and substring or input string from given string

# 20.write a program to replace substring using input string from a given string
string =input("enter your string")
n=input("enter your string to replace:")
n1=input("enter your string with wich string has to be replaced")
string=string.replace(n,n1)
print("string after replace")
print(string)

# write a program to find second max no in list
list1=[10,38,45,8364,325]
list2=list(set(list1))   # it use to remove duplicat value
list2.sort()        # sort is used to accending value
print("second max value is:",list2[-2])


