class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __mul__(self, other):
        return Fraction(self.a * other.a, self.b * other.b)

    def __add__(self, other):
        return Fraction(self.a * other.b + self.b * other.a, self.b * other.b)

    def __sub__(self, other):
        return Fraction(self.a * other.b - self.b * other.a, self.b * other.b)

    def __eq__(self, other):
        return self.a / self.b == other.a / other.b

    def __gt__(self, other):
        return self.a / self.b > other.a / other.b

    def __lt__(self, other):
        return self.a / self.b < other.a / other.b

    def __ne__(self, other):
        return not self.a / self.b == other.a / other.b

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"






f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
f_a1 = Fraction(3, 5)
f_b1 = Fraction(2, 7)
f_c1 = f_a1 + f_b1
assert str(f_c) == 'Fraction: 21, 18'
assert str(f_c1) == 'Fraction: 31, 35'
print('add test == OK')
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
print('mul test == OK')
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'
print('sub test == OK')
#
assert f_d < f_c  # True
print('lt test == OK')
assert f_d > f_e  # True
print('gt test == OK')
assert f_a != f_b  # True
print('ne test == OK')