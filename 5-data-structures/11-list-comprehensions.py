items = [
    ("product01", 6),
    ("product02", 9),
    ("product03", 14)
]

#! instead of using map and filter function we can use list comprehension

mapPrices = map(lambda item:item[1], items)
print(list(mapPrices))

filterPrices = filter(lambda item:item[1] <= 10, items)
print(list(filterPrices))

#! list comperhension

prices= [item for item in items if item[1] <= 10]
print(prices)