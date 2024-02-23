def add(x, y):
    return x + y


def substract(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


num1 = int(input('Please enter first number: '))

num2 = int(input('Please enter second number: '))

print(f'{num1} + {num2} = {add(num1, num2)}')
print(f'{num1} - {num2} = {substract(num1, num2)}')
print(f'{num1} * {num2} = {multiplication(num1, num2)}')
print(f'{num1} / {num2} = {division(num1, num2)}')
