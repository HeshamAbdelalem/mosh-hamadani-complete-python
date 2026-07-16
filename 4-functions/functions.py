#? how to declare function
# def sayHello():
#     print("Hello amigos!")

# sayHello()

#? function with arguments

# def sayHello(firstname, lastname):
#     firstname = firstname.capitalize()
#     lastname = lastname.capitalize()
#     print(f"Hello {firstname} {lastname}")
    
# sayHello("hesham", "Ali")

#? we have 2 types of functions 
#! 1.function that perform a task
#! 2.function that returns a value

#! this function will perform task and by default will return None

# def great(name):
#     print(f"Greeting {name}")
    
# great("Roka")
# print(great("Roka")) #! here we can see that the function returns None

# def makeGreat(name):
#     return f"Greating {name}"

# message = makeGreat("Hesham")
# print(message)
# print(makeGreat("Hesham")) #! here the function returned the string inside it not None


#? keyword arguments

# def increment(number, by):
#     return number + by

# print(increment(5,6))
# print(increment(number=6,by=3)) #! just to make it more readable

#? arguments default value

# def increment(number, by=1): #! here the user can ignore the second argument and it will present as 1 cuz it's the default value
#     return number + by
    
# print(increment(10))

#? xargs *args

# def incrementAll(*number): #!here we don't specify certain arguments but we leave it to be unconuntable
#     total = 0
#     for num in number:
#         total += num
        
#     return total

# print(incrementAll(4,3,4,3,4,5))

#? xarags **kwargs

# def userData(**user):
#     print(user["name"])
    

# userData(id = 1, name= "Abdallah", age = 8)

