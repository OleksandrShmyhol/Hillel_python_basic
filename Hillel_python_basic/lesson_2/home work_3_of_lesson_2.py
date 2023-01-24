user_number = int(input("Введіть 5-ти значне число:"))
number = user_number % 10 * 10000 + user_number // 10 % 10 * 1000 + user_number // 100 % 10 * 100\
         + user_number // 1000 % 10 * 10 + user_number // 10000 * 1
print(number)

