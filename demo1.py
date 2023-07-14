# 8.Write a program that input a string and ask user to delete a given word from a string.
text=input("enter your string:")
words=text.split(' ')
data=input("enter a word to delete:")
status = False
for word in words:
    if word == data:
        words.remove(word)
        status = True
if status:

    text= ' '.join(words)
    print("string after delation",text)
else:
     print("word is not in string.")

s=input("enter a sentence:")
print(s.title())
