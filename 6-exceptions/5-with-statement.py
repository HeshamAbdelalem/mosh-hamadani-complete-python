try: 
    with open("open.py") as file: #! the with statement handles the clostion of the file and we don't need finally statement
        print("file opened.")
    
    age = int(input("Age: "))
    agefactor =  10 / age
except (ValueError, ZeroDivisionError) as ex:
    print("Please Enter an integer only")
    print("this is the ex::" ,ex)
else:
    print("no exception were thrown")



print("program continue running and didn't stop like what happened when exception thrown")