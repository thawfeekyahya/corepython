# There are four types of arguments passing
# Positional
# Keyword
# Default
# Variable length

# Keyword argument example
def func(item,price):
    print(item,"---- PRICE",price)

func(price=20,item="Chapati")

def varfunc(*params):
    print("Passed in parameters are",params)

varfunc("Hello","World","Welcome","To","Python")

def varkeywordfunc(**paramkeyvalue):
    for x,y in paramkeyvalue.items(): # items() will give pairs of items
        print("Key= {},Value={}".format(x,y))

varkeywordfunc(firstname="Thawfeek",lastname="Yahya",rank=1)


