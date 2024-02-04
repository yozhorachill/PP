#Python Sets
#1st example
thisset = {"apple", "banana", "cherry"}
print(thisset)

#2nd example
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#3rd example
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

#4th example
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

#5th example
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#6th example
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#7th example
set1 = {"abc", 34, True, 40, "male"}

#8th example
myset = {"apple", "banana", "cherry"}
print(type(myset))

#9th example
thisset = set(("apple", "banana", "cherry")) 
print(thisset)



#Python - Access Set Items

#1st example
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#2nd example
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
  
  
  

#Python - Add Set Items

#1st example
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#2nd example
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
  
#3rd example
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)





#Python - Remove Set Items

#1st example
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
  
#3rd example
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#4th example
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#5th example
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#6th example
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)




#Python - Loop Sets

#1st example
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  






#Python - Join Sets

#1st example
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#2nd example
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#3rd example
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#4th example
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

#5th example
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

#6th example
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

#7th example
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

print(z)







