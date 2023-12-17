# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# newlist = [expression for item in iterable if condition == True]

array = list(x*2 for x in range(1,20) if x%2 == 0)
print(array)

