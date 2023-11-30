#Exponention assignment operator
a=2**4 # This implies 2^4
print(a)

#Floor division operator
b=5//2 # This returns only integer quotient , this is excluding the float value
print(b)

#In Python Relational operators can be chained
c=5<a>b # Implies 5>16 && 16 > 2
print(c)


#Logical Operators
# and
# or
# not

x=100
y=200

print("And Operator",x and y)
print("Or Operator",x or y)
print("Not Operator",not x)

#Membership Operators
# in
# not  in
list = [1,2,3,4,5]
for i in list: print(i)

print(5 in list)

print(8 not in list)
print(1 not in list)

# Idenity Operator
# Used to compare memory locations

a=4
b=4

print(id(a))
print(id(b))
