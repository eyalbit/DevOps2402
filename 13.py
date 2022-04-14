# import fibo
from fibo import fib as my_fib

#my_fib(1000)


def square(x):
    result = x * x
    return result
#print(type(square(5)))
def devide(a, b):
    result = a / b
a = square(5)
b = devide(10, 2)
#print(b)

from utills import my_print

#my_print(4)


def get_numeric(number):
    numners = ["zero", "one", "two", "three", "four"]
    if number < len(numners):
        return  numners[number]
    else:
        print("incorect")

number_from_user = int(input("type a number: "))
if  0 <= number_from_user < 5:
    print(get_numeric(number_from_user))