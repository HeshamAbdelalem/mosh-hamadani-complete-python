numbers = [1,2,3,4,100]

# first, second = numbers #! this will introduce an error too many valued to unpack

# first, second, *otherNumbers = numbers #! with this syntax it will take the first 2 values and assign them and the rest of the list will be assigned to new list (otherNumbers)
# print(otherNumbers)

#! what if we care about the first item and the last?
first, *otherNumbers, last = numbers
print(f"first:{first}, last:{last}, what between:{otherNumbers}")