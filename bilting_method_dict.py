car={'name':'BMW','color':'red','year':'2023'}

# get()  : retan value of perticular key
print(car.get('color'))

#keys()  : list of key present in your dictionary
print(car.keys())

#items()  : return list of element in group
print(car.items())
# it show in list all key value

# values
print("all values in list:",car.values())

#pop()
car.pop('color')
print(car)

#pop_items()  : it last key remove
car.popitem()
print(car)

d1={1:'a',2:'b',3:'c',4:'d'}
del d1[1]  # 1 is key
print(d1)

# clear()
d1.clear()
print(d1) # clear all data  # empty dict created

#update()
#it append one dict into anther dict
d1={'mon':'1','tues':'2','wen':'4'}
d2={'ther':'3','fir':'5','wen':'3'}
d1.update(d2)    #if same value in two dict than display last value means it update first  becouse we update d1
print(d1)

d3=(d1|d2) #it combain two dict
print(d3)

#fromkeys()     #it show first dict value consider key and second dect consider values but  all dict1 key pair with dict2 value only one value to all
dict1={1,2,3}
dict2={3}
dictionary=dict.fromkeys(dict1,dict2)
d=dict.fromkeys(dict1)
print(dictionary)
print(d)