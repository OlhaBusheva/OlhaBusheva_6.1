def add(x, y):
    return x + y


def substract(x, y):
    return x - y


num1 = int(input('Please enter first number: '))

num2 = int(input('Please enter second number: '))

print(f'{num1} + {num2} = {add(num1, num2)}')
print(f'{num1} - {num2} = {substract(num1, num2)}')
