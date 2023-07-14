# 1.1: Convert two lists into a dictionary
l1=[1,2,3,4]
l2=['rani','soni','mohini','sahana']
print(dict())
text=dict(zip(l1,l2))
print("zip function",dict)
print(text)


test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]

# Printing original keys-value lists
print("Original key list is : " + str(test_keys))
print("Original value list is : " + str(test_values))

# using zip()  pair key,value
# to convert lists to dictionary  dict()
res = dict(zip(test_keys, test_values))

# Printing resultant dictionary
print("Resultant dictionary is : " + str(res))

# 2.: Merge two Python dictionaries into one
d1={'name':'rohi','add':'latur','rollno':'1'}
d2={'emp_name':'rohini','add':'pune','salary':20000}
d3=d1.update(d2)
print("updated dictionary:")
print(d1)

# 3.3: Print the value of key ‘history’ from the below dictionary
'''sampleDict = {
      "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
               "history": 80
            }
        }
    }
}
'''
sampleDict ={"class":{"student":{"name":"Mike","marks":{"physics":70,"history":80}}}}
sampleDict["class"]={"student":{"name":"Mike","marks":{"pysics":70,"history":80}}}
sampleDict["class"]["student"]={"name":"Mike","marks":{"pysics":70,"history":800}}
sampleDict["class"]["student"]["marks"]={"pysics":70,"history":800}
print(sampleDict["class"]["student"]["marks"]["history"])

# 4.4: Initialize dictionary with default value

employees={'kelly','Emma'}
defaults={"designation":'developer','salary':8000}
new_dict={}
key = ('kelly','Emma')
new_dict=new_dict.fromkeys(key,defaults)
print(new_dict)

# 5. Create a dictionary by extracting the keys from a given dictionary

simple_dict={"name":"kelly","age":25,"salary":8000,"city":"new york"}
keys={"name","salary"}
res=dict()
for k in keys:
    res.update({k: simple_dict[k]})
print(res)

# 6.Delete a list of keys from a dictionary
# print(sample_dict)
simple_dict={"name":"kelly","age":25,"salary":"8000","city":"new youk"}
keys=["name","salary"]
for k in keys:
    simple_dict.pop(k)
print(simple_dict)

#7. Check if a value exists in a dictionary
simple_dict={'a':'100','b':'300','c':'200'}
if '200' in simple_dict.values():
 print("'200'is present in dict",simple_dict)

# 8: Rename key of a dictionary
student={'emp_name':'rohini','age':'21','add':'latur','salary':'20000'}
student ['name'] = student.pop('emp_name')
del student['name']
print(str("student"))

#9: Get the key of a minimum value from the following dictionary.

simple_dict = {'Physics': '82', 'Math': '65', 'history': '75'}
print(min(simple_dict,key =simple_dict.get))
#10: Change value of a key in a nested dictionary
sample_dict ={'emp1': {'name': 'Jhon', 'salary': '7500'},
              'emp2': {'name': 'Emma', 'salary': 8000},
              'emp3': {'name': 'Brad', 'salary': 6500}
              }
sample_dict['emp3']['salary'] = 8500
