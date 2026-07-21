#
#? [expression for item in items]

values = [] 
for x in range(1,5):
    values.append(x *2)

print(values)

values = [item * 2 for item in range(10, 15)] #! list comprehension
print(values)

#! we can also use comprehension with sets and dictionaries

valuesSet = {item * 2 for item in range(10,15)}
print(valuesSet)

valuesObj = {}

#! objects
for x in range(1,5):
    valuesObj[x] = x * 2
    
print(valuesObj)

valuesObj2 = {valuesObj[x]: x * 3 for x in range(1,5)}
print(valuesObj2)