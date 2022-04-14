from user_input import user_input
from addition import addition


def my_main():
    a = user_input()
    b = user_input()
    result = addition(a, b)
    print(result)

my_main()
