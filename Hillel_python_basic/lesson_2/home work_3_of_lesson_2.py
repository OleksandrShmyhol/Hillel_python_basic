user_number = int(input("Введіть 5-ти значне число:"))
five_number = user_number % 10
four_number = user_number // 10 % 10
third_number = user_number // 100 % 10
second_number = user_number // 1000 % 10
first_number = user_number // 10000
result = five_number * 10000 + four_number * 1000 + third_number * 100 + second_number * 10 + first_number * 1
print(result)
