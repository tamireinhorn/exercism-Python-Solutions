
from decimal import DivisionByZero
from math import sqrt, sin, cos, exp

class ComplexNumber:
    """Prototype of a complex number class for Exercism. 
    """
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
 
    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        return ComplexNumber((self.real * other.real) - (self.imaginary * other.imaginary), (self.imaginary * other.real) + (self.real * other.imaginary))

    def __sub__(self, other):
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __truediv__(self, other):
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        a, b = self.real, self.imaginary
        c, d = other.real, other.imaginary
        square = c ** 2 + d ** 2 
        if square == 0:
            raise DivisionByZero("Attempting to divide by zero.")
        real_part = ((a*c) + (b * d)) / square
        imaginary_part = ((b*c) - (a*d)) / square 
        return ComplexNumber(real_part, imaginary_part)

    def __abs__(self):
        return sqrt(self.imaginary ** 2 + self.real ** 2)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        a, b = self.real, self.imaginary
        exp_a = exp(a)
        return ComplexNumber(exp_a * cos(b), exp_a * sin(b))
    #The __r__ is basically done when we have an operation like: non_class_object operation class_object.
    # For comutative operations, this means that add and mult can be the same
    # For subtraction and division, we need to change the return for it to be other / self
    __radd__ = __add__
    __rmul__ = __mul__

    def __rtruediv__(self, other):
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        return other / self

    def __rsub__(self, other):
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        return other - self

  
