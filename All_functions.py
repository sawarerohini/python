# 1.Write a Python function to find the Max of three numbers.
def max_of_two (x,y):
    if (x>y):
        return x
    return y
def max_of_three(x,y,z):
    return max_of_two(x ,max_of_two (y,z))
print(max_of_three(5,-7,1))

# 2.Write a Python function to sum all the numbers in a list.
def sum_of_list (l):
  total =0
  for value in l:
      total=total+value
  return total
my_list= [2,3,4,56,9]
print ("the sum of my_list is:",sum_of_list(my_list))

# 3.Write a Python function to multiply all the numbers in a list.l2=[34,33,53,5]
def multi_of_list (i):
    total = 1
    for value in i:
        total=total+value
    return total
my_list=[34,33,53,5]
print("multiplication of my list:",multi_of_list(my_list))

# 4.Write a Python program to reverse a string using function.
text = "i am learn python"[::-1]
print(text)

# 5.Write a Python function to check whether a number falls in a given range.
def test_range (n):
    if n in range(0,8):
        print("the no in range:",n)
    else:
        print("the no is outsaid the range.")
test_range (5)

#6. Write a Python function that accepts a string and calculate the number of upper case letters
#and lower case letters

def up_low(string):
    upper =0
    lower =0
    for char in string:
      if char.islower():
        lower +=1
      elif char.isupper():
        upper +=1
      else:
        pass
    return (lower,upper)
print(up_low("My Name Is Rohini,I Im From Latur District"))

