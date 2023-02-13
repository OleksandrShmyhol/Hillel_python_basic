import random
from random import randint


def common_elements():
    lst1, lst2 = [], []
    for _ in range(randint(1, 10)):
        lst1.append(random.randrange(3, 90, 3))
        lst2.append(random.randrange(5, 90, 5))
    lst1, lst2 = set(lst1), set(lst2)
    result = lst1.intersection(lst2)
    print(result)
    return result
