# Operator Overloading

class BookA():

    def __init__(self):
        self.pages = 200


class BookB():

    def __init__(self):
        self.pages = 300

    def __add__(self, other): # __add__ is special method for + operator, here its overloaded in BookB, so only b2 + b1 will work, b1 + b2 will throw error 
                              # opeator overloading not defined in BookA

        return self.pages + other.pages

b1 = BookA()
b2 = BookB()

print("Total Pages", b2 + b1)
