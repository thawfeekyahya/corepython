import array as Array

"""
NOTE: Python does not have increment and decrement operators ( ++,--)
"""
# Arrays in python

"""
Array type codes
b -> signed int     // 1 byte             \n        
B -> unsigned int   // 1 byte             \n       
i -> signed int     // 2 byte             \n       
I -> unsigned int   // 2 byte             \n       
l -> signed int     // 4 byte             \n       
L -> unsigned int   // 4 byte             \n       
f -> floating point // 4 byte             \n        
d -> double precision floating // 8 byte  \n    
u -> unicode charcter // 2 byte           \n  

"""
a = Array.array("i",[4,5,6,7])

# lists in python
list = ["Thawfeek",1,2,3,"Yahya"]
for i in list: print(i)

# Non-mutable arrays using tuple
tuple = ("Thawfeek",1,2,3,"Yahya")
for i in tuple: print(i)

# mutatation won't work in tuple
# tuple[2] = 0  # This will throw error

# Range : Non-mutable number sequences

r = range(10)

for i in r: print(i)

# Custom start values in range

# Start value | End value | Step value

r = range(30,40,2)
for i in r: print(i)


# Slicing the array
print("Sliced Arrayy value -> ",r[0:3])

# Set is unordered list with unique values , ie) same values are not duplicated

s = {10,20,30,40,50,60,70,80,90}
for i in s: print(i)

charSet = set("Hello")
print(charSet)

#Adding value to existing set
s.update([100,100])

#remvoing value from existing set
s.remove(30)

# Dictionary / Map

dict = {"Thawfeek":35,"Sarah":5,"Hamzah":1,"Yasmin":30}
print(dict)
print("Thawfeek age is ->",dict["Thawfeek"])
