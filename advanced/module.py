# Python module to calculate salary of a employee

def da(basic):
    """ da is 80% of basic sqlary """
    da = basic*80/100
    return da

def hra(basic):
    """ is 15^ of basic salary """
    hra = basic * 15/100
    return hra

def pf(basic):
    """ pf is 12% of basic salary """
    pf = basic * 12 /100
    return pf

def itax(gross):
    """ tax is calculated at 10% on gross """
    tax = gross*0.1
    return tax
