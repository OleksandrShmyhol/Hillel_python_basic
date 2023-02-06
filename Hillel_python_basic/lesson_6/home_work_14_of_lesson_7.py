number = int(input())
lst = list(str(number))
summ = 0
if number < 1:
    print("Число має бути більше 0")
else:
    while number >= 10:
        if summ not in range(1, 10):
            summ = 1
            for el in lst:
                summ *= int(el)
            lst = list(str(summ))
        number = summ
    print(number)
