# Abstract class demo

from abc import ABC, abstractmethod # import Abstract Base Class Module 'ABC'

class AbsClass(ABC):
    
    @abstractmethod
    def calculate(self,x):
        pass # Empty function body , skip execution using 'pass' keyword

class Concrete1(AbsClass):
    def calculate(self,x):
        print("Square value = ",x*x)

class Concrete2(AbsClass):
    
    def calculate(self,x):
        print("Cube value = ",x**3)


square = Concrete1()
cube   = Concrete2()

square.calculate(2)
cube.calculate(2)


