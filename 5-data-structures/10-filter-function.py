items = [
    ("product01", 6),
    ("product02", 9),
    ("product03", 14)
]

#! we need to return items that costs less than 10 dollars
#! here's the coplex way

# def lessThanTen():
#     for item in items:
#         if item[1] < 10:
#             print(item[1])
        
# lessThanTen()

#! and here we will use lambda function + built in filter function

x = filter(lambda item: item[1] < 10, items) 

print(x) #! it will return filter object , which is iterable so we can convert it to a list

filteredlist = list(filter(lambda item: item[1] < 10, items) )
print(filteredlist)
