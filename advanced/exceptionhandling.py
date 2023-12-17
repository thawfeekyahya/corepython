# Exception handling demo

try:
    name = input("Enter filename")
    f = open(name,'r')

except IOError:
    print("File not found ",name)
else:
    n = len(f.readlines())
    print(name,"has ",n," lines")
    f.close()


try:
    date = eval(input("Enter date"))    # 'eval' keyword is used to dynamically take input, ie) 12/12/23 as date object
except SyntaxError:                     # Here except stands for 'Exception'
    print("Invalid Date format , Enter as YY,MM,DD")
else:
    print("You Entered", date)
   
