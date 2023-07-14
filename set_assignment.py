#Exercise 1: Add a list of elements to a set
set={1,2,3,54,56}
set.add('sunday')
print(set)
#Exercise 2: Return a new set of identical items from two sets
s1={1,2,3,45,5,6,678,0}
s2={3,2,4,5,1,8,9,}
print(s1.intersection(s2))
#Exercise 3: Get Only unique items from two sets
s1={1,2,3,4}
s2={6,7,89,1,2,3}
print(s1.symmetric_difference(s2))
#Exercise 4: Update the first set with items that don’t exist in the second set
s1={1,20,3,4}
s2={'python',1,3,50,'java'}
s1.difference_update(s2)
print(s1)
#Exercise 5: Remove items from the set at once
s={3,40,67,8,9}
print(s.remove(8))
print(s)
#Exercise 6: Return a set of elements present in Set A or B, but not both
s1={10,20,30,40}
s2={80,60,50,20,10}
print(s1.symmetric_difference_update(s2))
print(s1)
#Exercise 7: Check if two sets have any elements in common. If yes, display the common elements
s1={1,2,3,4}
s2={4,6,7,1,3}
if s1.isdisjoint(s2):
    print("in thise set have not comman value")
else:
    print("thise set have comman value")
print(s1.intersection(s2))
#Exercise 8: Update set1 by adding items from set2, except common items
s1={'rohini','sahana','pratiksha','priyanka'}
s2={'pratiksha','mohini','divya','mayuri'}
print(s1.symmetric_difference_update(s2))
print(s1)
#Exercise 9: Remove items from set1 that are not common to both set1 and set2
s1={1,2,3,4}
s2={6,7,8,3,2}
print(s1.intersection_update(s2))
print(s1)
