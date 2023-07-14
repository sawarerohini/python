#1. Write a Python program to check that a string contains only a certain set of characters (in this
#case a-z, A-Z and 0-9)
string ="rohiNI1234"
import re
reg ="[a-z][A-Z][0-9]"
if re.search(reg,string):
    print("correct")
else:
    print("not")

#2. Write a Python program to find sequences of lowercase letters joined with a underscore
import re
def text_match(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("aab_cbbbc"))
print(text_match("aab_abBbc"))
print(text_match("Aaab_abbbc"))

#3. Write a Python program that matches a word at the beginning of a string.
string ="i am leArn python"

patterns ="[A_Z]*[a_z]*"
if re.match(patterns,string):
    print("match patterns")
else:
    print("not match")

# 4. Write a Python program where a string will start with a specific number
string ="1rohini"
patterns="[0_9]*"
if re.match(patterns,string):
    print("start with specific no")
else:
    print("not start with specific no")

# 5. Write a Python program to check for a number at the end of a string
string ="saware rohini 1234"
pattrens="[0_9]*"
if re.match(pattrens,string):
    print("no at the end of string")
else:
    print("no at not end of string")




