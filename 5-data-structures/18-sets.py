numbers = [1,2,5,6,7,9,9,1,5]

#! if we have set of value inside a list with duplicate values and we only wana use uniqe values we use set
#! set is unorder of uniqe items , we can  have duplicate and we can't access them use index 

uniqueNums = set(numbers)
uniqueNums.add(10)
uniqueNums.remove(5)


print(uniqueNums) #! it returs a set of only unique values 

#! but sets shine at here

firstSet= {1,2,3,4,5}
secSet= {6,7,8,9,10,5,4}
unionSet = firstSet | secSet #! here we union the 2 sets

print("unionSet: ", unionSet)

print(firstSet | secSet) #! here we union the 2 sets
print(firstSet & secSet) #! will return What do they have in common
print(firstSet - secSet) #! will Take everything from firstSet and Remove anything that also exists in secSet - The order matters! 
print(firstSet ^ secSet) #! will Give everything except the common elements.