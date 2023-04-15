# adding the function for addition to add two number.
def add(x,y):
    return x + y
#adding the function for subtraction of two numbers.
def sub(x,y):
    return x - y
#adding the function for multiplication of two numbers.
def mul(x,y):
    return x * y
#adding the function for division of two numbers.
def div(x,y):
    if y==0:
        raise ValueError('cannot divide by 0')
    return x / y
def mod(x,y):
    return x%y
