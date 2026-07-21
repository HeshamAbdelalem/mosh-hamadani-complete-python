letters = ["a", "b", "c"]

# letters.index("y") #! in most C like language we recevie -1 not an error like python

#! to avoid getting errors we can use .count() or keep using index but validate it with if statement

if "y" in letters:
    print(letters.index("y"))
    
print(letters.count("y"))