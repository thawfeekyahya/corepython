# Custom exception class demo

class MyException(Exception): # inherit Exception built-in class type
    def __init__(self,arg):
        self.msg = arg

def check():
   x = int(input("Enter value"))
   if(x < 10):
       raise MyException("Value is less than 10")


try:
    check()
except MyException as me:
    print(me)


