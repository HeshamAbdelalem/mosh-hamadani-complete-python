letters = ["a", "b", "c"]

# for letter in letters: 
#     print(letter)

#! what if we wana return the index and the value on that index
for letter in enumerate(letters):
    print(letter)
#! now it will return tuples

#! what if we don't wana the tuple structure? we can unpack it just like lists
for index,letter in enumerate(letters):
    print(index, letter)