try: 
    age = int(input("Age: "))
except ValueError as ex:
    print("Please Enter an integer only")
    print(ex)
else:
    print("no exception were thrown")

print("program continue running and didn't stop like what happened when exception thrown")