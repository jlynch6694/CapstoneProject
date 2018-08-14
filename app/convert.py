import math
from app.forms import currencyForm, InputGDP


def convertThis(q, v):
    if q == 'US Dollar':
        v = v
    elif q == 'Chinese Yuan':
        v = [ num * 0.15 for num in v ]
    elif q == 'Canadian Dollar':
        v = [ num * 0.76 for num in v]
    elif q == 'Mexican Peso':
        v = [num * 0.053 for num in v]
    elif q == 'Japanese Yen':
        v = [num * 0.009 for num in v]
    elif q == 'Euro':
        v = [num * 1.17 for num in v]
    elif q == 'South Korean Won':
        v = [num * 0.00089 for num in v]
    elif q == 'British Pound':
        v = [num * 1.31 for num in v]
    elif q == 'Indian Rupee':
        v = [num * 0.0015 for num in v]
    elif q == 'New Taiwan Dollar':
        v = [num * 0.033 for num in v]
    print(q, v)
    return v

class CalculateGDP ():
    def __init__(self, num1, num2, num3, num4, num5):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4
        self.num5 = num5
        self.x = (num1 + num2 + num3 - num4)/num5

    def formatnum(self):
        return '{:,.2f}'.format(self.x)


    def printinfo(self):
        if self.num1 > 0 and self.num1 < 2000000000:
            return('This company is a small-cap company')
        elif self.num1 > 2000000000 and self.num1 < 10000000000:
            return('This company is a mid-cap company')
        elif self.num1 > 10000000000:
            return('This company is a large-cap company')
