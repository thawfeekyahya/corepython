print("Enter your name")
name=input()

print("Your name is %s"%name)
print("Enter 2 numbers for addition")
a=int(input("Enter first number "))
b=int(input("Enter second number "))
print("The result of a+b is ",a+b)

# Accepting multiple inputs as int using comma as seperator
# 1,2,3
var1,var2,var3=[int(x) for x in input("Enter three number for multiplication ").split(",")]
print(var1*var2*var3)

#Accepting runtime datatype using eval
list = eval(input("Enter the list of values:"))
print(list)
