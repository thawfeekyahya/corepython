## Namespaces
   In Python there are 2 kind of namespaces 
   
   1. class namespace
   2. instance namespace

## Class Namespace
   In class namespace  the names are mapped to class variables.
   The class namespace is invoked using the the class name , ie) if the class name is Test ,then

   ```
   Test.var1 = 100 // This is using classnamespace
  
   ```

## Instance Namespace
   In Instance namespace the names are mapped to instance variables. 
   The instance namespace is invoked using the instance name id) if the instance name is 'a' , then

   ```
   Test = a()
   a.var1 = 200 // This is using instance namespace

   ```

## Class variables Vs Instance variables

   When invoking either of class or instance variables , apropriate namespace needs to be utilized .

```
   class Test:
	x = "Hello"
        __init__(self,value):
		self.a = value
   
    t1 = Test(100) 
    t2 = Test(200)

    print(t1.a) // Will print instance variable a with the value 100
    print(t2.a) // Will print instance variable a with the value 200

    t1.x = "Good Morning"   // WRONG: This is wrong way of calling the class varible using instance namespace // This will cause shadow effect
    Test.x = "Good Morning" // CORRECT: While calling class variable , class namespace has to be used ie) 'Test.x' 
    
    print(t1.x) // Will print "Good Morning" 
    print(t2.x) // Will print "Hello" // class variable is unaffected even after changing it, this is because of using wrong namespace 
   
```

## Decorator @classmethod
   
   When we need to create a class level 'static' method we need to use the decorator '@classmethod' on the function

```  
  class Test:

   	@classmethod
   	def sayHello(cls,name): // NOTE: 'cls' refers to the class namespace and the decorator '@classmethod' is required for calling this method in class namespace
   	print("Hello",name)

  Test.sayHello("Stark") //  class namespace is used to invoke the method 

```

## Decorator @staticmethod
  
   When need to process some info which are not related either to class or instance then we need to utilize staticmethod

```
  class Test:

    n=0

    @staticmethod
    def noObjects():
	print("No. of instance created:", Test.n)

    obj1 = Test()
    obj2 = Test()
    obj3 = Test()

    Test.noObjects()
