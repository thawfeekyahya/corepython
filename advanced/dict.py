# Dictionary in Python

dict = {"Name":"Thawfeek","Company":"MBRDI","Location":"Bangalore"}

for key,value in dict.items():
    print("Key is ",key)
    print("value is ",value)

# Dynamic key value

dict = {}

x = int(input("Enter the number for items you want to enter"))
for i in range(x):
    key = input("Enter key")
    value = input("Enter value")
    dict.update({key:value})

print(dict)

