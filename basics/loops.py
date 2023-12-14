# Nested loops

#for i in range(1,10):
#    for j in range(1,i+1):
#        print("*",end="")
#
#    print()

# another way to do the above using more elegant approach

for i in range(10):
   print("*"*i)

# print triangle

space=40
for i in range(10):
    # first print the required space minus i then add * multipled by i
    print(" "*(space-i)+"* "*i)


# print tables
print("\n"*3)
for i in range(1,11):
    for j in range (1,11):
        print("{:8}".format(i*j), end="")
    print()

#While with continue

x=0
while x<10:
    x+=1
    if x>5:
        print("x is > 5",x)
        continue
    print("x=",x)
print("Out of loop")


# Pass statement // Used to skip , do nothing

num = [1,2,3 -5,-4,-2,7,8,9]
for i in num:
    if(i>0):
        pass
    else:
        print("Negative value is",i)

