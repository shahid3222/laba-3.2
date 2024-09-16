class Complex:
    def __init__(self, real=0.0, imaginary=0.0):
        self.real = real
        self.imaginary = imaginary
    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)
    def __mul__(self, other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return Complex(real_part, imaginary_part)
    def __truediv__(self, other):
        real_part = (self.real * other.real + self.imaginary * other.imaginary)
        imaginary_part = (self.imaginary * other.real - self.real * other.imaginary)
        return Complex(real_part, imaginary_part)
    def __str__(self):
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {-self.imaginary}i"
if __name__ == "__main__":
    c1 = Complex(2, 3)
    c2 = Complex(1, 4)

    print("Комплексные числа",c1,",",c2)
    print("Сложение:", c1 + c2)
    print("Вычитание:", c1 - c2)
    print("Умножение:", c1 * c2)
    print("Деление:", c1 / c2)

