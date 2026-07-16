def increment(*nums):
    total = 0
    for num in nums: 
        total += num
    return total


print("start")
print(increment(1,2,3,4,5))
print("End")