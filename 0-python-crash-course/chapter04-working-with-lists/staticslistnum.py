# get the sum of the numbers from 1 to 10
# total = 0

# for number in range(1, 11):
#     total += number
    
# print(total)

# print(sum(list(range(1,11))))

#get the min number of a list

numbers = [900,123,46,87,68,147,5,2,-5,87,63,31,79,12,167,217,0,97,13,794,3,469,800,7]

def findMin(listOfNums):
    minNumber = listOfNums[0]

    for num in listOfNums:
        if minNumber >= num:
            minNumber = num
            
    print(minNumber)
    
def findMax(listOfNums):
    minNumber = listOfNums[0]

    for num in listOfNums:
        if minNumber <= num:
            minNumber = num
            
    print(minNumber)


# findMin(numbers)
# findMax(numbers)

listofExpNum = [num**2 for num in range(1,11)]

print(listofExpNum)