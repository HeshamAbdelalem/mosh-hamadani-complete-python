#
#! here we wana put the prices somewhere else , a list 

items = [
    ("product1", 60),
    ("product2", 34),
    ("product3", 43)
]


 

# for item in items:
#     prices.append(item[1])
    
prices = list(map(lambda item:item[1], items))

print(prices)