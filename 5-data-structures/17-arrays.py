from array import array

#! we use arrays when we dealing with large sequence of numbers and ecounter performance issues , otherwise we use lists and tuples
#! every value inside the array should be the same type , we specify type on the first argument
#! https://docs.python.org/3/library/array.html     - here we can find the C type and it's typecode
arrayOfNums = array("i" , [1,23,45,67])


print(arrayOfNums[2])