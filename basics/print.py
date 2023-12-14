# Print tricks
# Print using * operator

print("Hello World"*5,"another","and another",sep="----",end="\t")
print("Python")


# Print formated strings
# print("formated string" % (variable list))

x=10
print("value= %i" % x)

x,y=10,15
print("X= %i Y=%d" % (x,y)) # parentheses are required for more than one variable

name="Thawfeek"

print("Hello %s" % name)

#Using spaces in print %20s

print("Welcome  %20s" % name)

print("Welcome  %-20s" % name)


#Print single charcters

print("First letter %c and last letter %c" % (name[0],name[7]))


#Print using format

n1 = 100
print("Number n1 is={0}".format(n1))

print("NUmber n1 ={one}".format(one=n1))

print("With Space {:20}".format(n1))

