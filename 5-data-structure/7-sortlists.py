#a
#! here we have sort(), sort(reverse=True) , reverse() , sorted()
numbers = [32,79,6,4,87,10]

numbers.sort()
print(sorted(numbers)) 
print(numbers)

#! what if we have a list of tuples, how can we sort them ? we need to add a function does that

items = [
    ("product1", 60),
    ("product2", 34),
    ("product3", 43)
]

items.sort()
print(items) #! nothing changed

#! here we can implement function for this purpose
def sort_tuple(item):
    return item[1]

items.sort(key=sort_tuple)
print(items)