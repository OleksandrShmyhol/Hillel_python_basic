import numbers


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        raise TypeError('Разные типы данных')

    def __add__(self, other):
        if isinstance(other, Rectangle):
            area = self.get_square() + other.get_square()
            height = area/self.width
            return Rectangle(self.width, height)
        raise TypeError('Разные типы данных')

    def __mul__(self, n):
        if isinstance(n, numbers.Real):
            s = self.get_square() * n
            height = s/self.width
            return Rectangle(self.width, height)
        raise TypeError('Разные типы данных')
    def __str__(self):
        return f'Wight: {self.width};\nHeight: {self.height};'


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8
assert r2.get_square() == 18
r3 = r1 + r2
assert r3.get_square() == 26
try:
    r4 = r1 + 1
except TypeError as error:
    assert str(error) == "Разные типы данных"
print('add tests == OK')


r5 = r1 * 4
r6 = r1 * 6
r7 = r1 * 4
assert r5.get_square() == 32
assert r6.get_square() == 48
print('mul tests == OK')

assert (r5 == r7) == True
assert (r3 == r6) == False

print("bool tests == OK")