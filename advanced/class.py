class Test:

    var1 = 10

    def __init__(self):
        self.name = "Thawfeek"
        self.location = "Bangalore"
        self.__privateVariable = 35 # By marking with '__' double underscore variable can act as private

    def display(self):
        print(self.name)
        print(self.location)
   
    @classmethod
    def modify(cls):
        cls.var1 += 10 # Note here 'cls' is special keyword which points to this class , kind of static 

        
t1 = Test()
t2 = Test()

t2.var1 = 30
t2.d = 5
print(t1.var1) # Here t2 is modified but same value will be refelected in t1
print(t2.var1)
print(t2.d)
