try: 
    file = open("app.py")
    age = int(input("Age: "))
    agefactor =  10 / age
except (ValueError, ZeroDivisionError) as ex:
    print("Please Enter an integer only")
    print("this is the ex::" ,ex)
else:
    print("no exception were thrown")
finally: 
    file.close() #! here we close the opened file, network connection or database


print("program continue running and didn't stop like what happened when exception thrown")