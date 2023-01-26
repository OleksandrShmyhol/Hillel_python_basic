print("Введіть перше число:")
number1 = float(input())
print("Введіть друге число:")
number2 = float(input())
print("Введіть оператор (+, -, *, /):")
operator = input()
if operator == '+':
    print(number1 + number2)
elif operator == '-':
    print(number1 - number2)
elif operator == '*':
    print(number1 * number2)
elif operator == '/':
    if number2 == 0:
        print("На 0 ділити не можна!")
    else:
        print(number1 / number2)
elif operator not in ['+', '-', '*', '/']:
    print("Ви ввели некоректний оператор! Почніть спочатку і введіть один із операторів: +, -, *, /")
