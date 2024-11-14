from operations import add, subtract, multiply, divide
from util import checkOper

def calc():
    while True:
        expression = input("Введіть 'exit' для виходу з программи або будь-яке число: ")
        
        if expression.lower() == "exit":
            print("вихід")
            break

        try:
            num1 = float(expression)
        except ValueError:
            print("Неправильне число")
            continue

        operation = input("Введіть операцію (+, -, *, /): ")
        
        if not checkOper(operation):
            print("Неправильна операція")
            continue

        try:
            num2 = float(input("Введіть друге число: "))
        except ValueError:
            print("Неправильне число")
            continue

        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)

        print("Результат =", result)