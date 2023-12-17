# import user-defined module // module.py
import module as Employee

basic = float(input("Enter basic salary: "))

gross = basic + Employee.da(basic) + Employee.hra(basic) # NOTE: Alias Employee module is defined in module.py 
print("Your Gross Salary {:10.2f}".format(gross))
