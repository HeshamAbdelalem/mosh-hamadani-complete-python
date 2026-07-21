# 
#! lambda function is a simple one anonymous function that we can pass to another functions

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

items.sort(key=lambda item:item[1])
print(items)