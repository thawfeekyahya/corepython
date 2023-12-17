# Inheritance Demo

from parent import Parent # import module containing the parent class

class Child(Parent): # NOTE: 'Parent' parameter inside class object, this denotes this class inherits from a class called 'Parent'

    def __init__(self,name,family): # Accept parent parameter in the child constructor
        super().__init__(family) # Calling parent class constructor using 'super()' method
        self.name = name
        

    def setName(self,name):
        self.name = name 

    def getName(self):
        return self.name


c = Child("Tony","Stark")
print(c.getName())
print(c.getFamily())


