#we can define dictionaries by 2 ways

point = {"x":1, "y":2}
point = dict(x=1, y=2)

print(point["y"])
print(point)

#print(point["z"]) #! to avoid getting errors in our interpreter we can use instead if statement to check or get
if "a" in point:
    print(point["a"])
    
print(point.get("z")) #! it will return None , we can also change if false

print(point.get("z", 0))