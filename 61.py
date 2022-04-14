# for i in range(100):
#    print(i)


try:
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    result = a / b
    print(result)
except ZeroDivisionError as e:
   # print(f"something went wrong: {e.args}")
   print(f"could not devide by zero")
except ValueError as e:
    print("one of the variables is not a number")
except BaseException as e:
    print(f"somthing went wrong: {e.args}")
print("finished")

