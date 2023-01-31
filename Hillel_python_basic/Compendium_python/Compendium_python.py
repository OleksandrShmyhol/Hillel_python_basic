# Python = об'єктно-орієнтована мова програмування!
# Всі сущности в Python - об'єкти.
# Об'єкт = екземпляр класу.
# Клас = шаблон або прототип для створення об'єкту.
# На основі одного класу можна створити багато об'єктів.
# У кожного об'єкта є атрибути.
# Атрибут об'єкту називається мотодом, якщо його значення - функція.
#
# Вирази (exprassions). Результатом виразу є значення певного типу.
#
# Інструкція (statements). Інструкція виконують дію (створює функцію, запускає цикл і тд.):
# my_name = 'Alex'  # Присвоєння значень.
# Умовна інструкція:
# if my_name:
#      print(my_name)
#
#
#
#---------------------------------------------------------------------------------------------------------------------
# Основні типи в Python:
#
# Строка: str 'Alex'. Всі строки = екземпляри класу Строка - str (string).
# Якщо слово одне - строки пишуться в одинарних лапках 'Alex', якщо два і більше в подвійних "Alex" лапках.
#
# Ціле число: int 10. Всі цілі числа = екземпляри класу Ціле число - int (integer).
# Всі плюсові, мінусові числа а також 0 є екземплярами класу int.
#
# Логічний тип: bool True. У логічного типу є тільки 2 значення: True or False. Клас називається - bool (boolean).
#
# Список: list [1, 2, 3]. В списку можна зберігати елементи різних типів. Клас називається - list.
# При створенні списку потрібно використовувати квадратні дужки []. Значення в списку розділяються комами.
#
# Словник: dict {'min': 5, 'max': 8}. При створенні словника потрібно використовувати фігурні дужки {}.
# Значення в словнику розділяються комами. Кожен елемент в словнику складається з ключа та його значення.
# Назви ключів мають знаходитись між одинарними або подвійними лапками.
#
#---------------------------------------------------------------------------------------------------------------------
# Вбудовані функції в Python.
#
# print("Hello Python") - Вивести в консоль значення вказане в лапках.
# type(32) - Це корисна вбудована функція у Python, за допомогою якої можна отримати тип даних змінної.
# id() - Повертає унікальний ідентифікатор для зазначеного об'єкта - значення його адреси в пам'яті.
# len() - Це найпопулярніший спосіб отримати довжину ітерабельного об'єкта.
# sum() - Обчислює суму елементів послідовності вказану в аргументах.
# input() - Отримує від користувача рядок тексту.
# round() - Поверне вам плаваюче число, яке буде округлено до десяткових знаків, які вказані як вхідні дані. 10.2 -> 10.
# min() - Знаходить найменший елемент в послідовності.
# max() - Знаходить найбільший елемент в послідовності.
# int() - Створює нове ціле число з рядка або числа з плаваючою крапкою
# str() - Преобразовує об'єкт в строку.
# bool() - За допомогою цієї функції можна перевірити істинність або брехливість любого значення.
# input() - Попросити у користувача ввести певні дані в терміналі. Повертає введені дані користувачем як Строка (str).
# dir() - Отримати назви всіх атрибутів об'єкта вказаного в лапках.
#