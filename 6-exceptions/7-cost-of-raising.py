from timeit import timeit   #! this module calculate the time that python code take to execute


code1 =""" 
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("age cannot be 0 or less.")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
    """
    
code2 =""" 
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age

xfactor= calculate_xfactor(-1)
if xfactor == None:
    pass
    """
    
print("time that took to execute code1 for 10000 times::",timeit(code1, number=1000000)) 
print("time that took to execute code2 for 10000 times::",timeit(code2, number=1000000)) 
