# Global & Local variables inside a function

a=1
def func():
    global a # global keyword is used to denote the global variable 'a'
    print("Global a is",a)
    a = 2

func()
print("A in global scope changed to",a)

# using globals() method to access global elements

def func2():
    a=5
    x=globals()["a"]
    print("local a is",a)
    print("global a is",x)

func2()


# Anonymous function
# lambda has a implicit return statement , hence user MUST NOT declare return keyword in lambda function

f = lambda x: print("Squared is ",x*x)  # lambda keyword is used to denote the Anonymous function in python
f(5)

# Lambda along with list filter

lst = [0,1,2,3,4,5,6,7,8,9,10]
lst2 = list(filter(lambda x: (x%2 == 0),lst))
print("Filtered list",lst2)


# Lamda along with map // map is similar to filter except the function is carried on each element
lst = [1,2,3,4,5]
lst1 = list(map(lambda x: x*x*x,lst))
print("Mapped list values ",lst1)


# Decorator keyword '@' // used to implement decorator pattern in a function

def decor(fun):
    def inner():
        value = fun()
        return value + 2
    return inner

def decor2(fun):
    def inner():
        value = fun()
        return value * 2
    return inner


@decor  # NOTE: 'decor' keyword to indicate this function has decorator applied to it
@decor2 # Multi-Decorated function
def num(): 
    return 10

print("Decorated value",num())

# Generator functions // using yield statement , a function can generate required values

def mygen(x,y):
    while x<=y:
        yield x # NOTE: 'yield statement'
        x+=1
print("Generator / Yielding")
gen=mygen(5,10)
list1 = list(gen)
print(list1)

