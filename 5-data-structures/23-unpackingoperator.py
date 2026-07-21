list1 = [1,2,3,4,5,6]
list2 = [7,8,9,10]

print(list1)
print(*list1)

print(*"Hello")

combinedList = [*list1, *list2]
print(combinedList)

#! we can also use the unpacking operator to unpack objects

first = {"x": 1}
second = {"x": 10, "y":20}

combinedObj = {**first, **second , "z": 5}
print(combinedObj)