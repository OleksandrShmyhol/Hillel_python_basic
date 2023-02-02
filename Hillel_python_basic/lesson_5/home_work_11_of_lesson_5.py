answer = 0
while answer == 0:
    number1 = 0
    number2 = 0
    while number1 + number2 == 0:
        print("Введіть перше число:")
        number1 = input()
        if not number1.isdigit():
            number1 *= 0
            print("Ви ввели не число! Спробуємо ще раз.")
            break
        else:
            number1 = float(number1)

        print("Введіть друге число:")
        number2 = input()
        if not number2.isdigit():
            number2 *= 0
            print("Ви ввели не число!")
            break
        else:
            number2 = float(number2)

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
        else:
            print(
                "Ви ввели некоректний оператор! Почніть спочатку і введіть один із операторів: +, -, *, /")
    print("Бажаєте повторити розрахунок? Напишіть 'Yes'")
    if input() == 'Yes':
        continue
    else:
        print("До нових зустрічей!)")
        break
