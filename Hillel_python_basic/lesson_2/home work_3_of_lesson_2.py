user_number = int(input("Введіть 5-ти значне число:"))
first_number = user_number % 10
second_number = user_number // 10 % 10
third_number = user_number // 100 % 10
four_number = user_number // 1000 % 10
five_number = user_number // 10000
print(first_number, second_number, third_number, four_number, five_number)
