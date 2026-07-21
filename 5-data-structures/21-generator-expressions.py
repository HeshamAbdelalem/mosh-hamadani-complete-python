from sys import getsizeof

#! in situation where u deal with large set of values or infinite stream of data
#! we use generator object not list so we can save our memory

# values = [x for x in range(1000000000)]
# print(getsizeof(values))

valuesTuples = (x for x in range(1000000000))
print(getsizeof(valuesTuples))

#! what if we wana get the length 
#! we receive this error: TypeError: object of type 'generator' has no len()

print(len(valuesTuples))
