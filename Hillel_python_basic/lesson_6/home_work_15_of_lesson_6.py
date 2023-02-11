day = ['днів', 'день', 'дні']
word = ''
number = int(input("Давайте порахуємо період часу на основі кількості секунд. \n"
                   "Введіть кількість секунд від 1 - 8639999:"))
days, hours, minutes = 0, 0, 0
remainder = 0
if number in range(1, 8640000):
    days, remainder = divmod(number, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, remainder = divmod(remainder, 60)
    if days % 10 == 1 and days % 100 != 11:
        word = day[1]
    elif days % 10 in range(2, 5) and days % 100 not in range(12, 15):
        word = day[2]
    else:
        word = day[0]
    print(str(days) + ' ' + word + ', ' + str(hours).zfill(2) + ':' + str(minutes).zfill(2) + ':' +
          str(remainder).zfill(2))
else:
    print("Введіть число від 1 до 8639999")
