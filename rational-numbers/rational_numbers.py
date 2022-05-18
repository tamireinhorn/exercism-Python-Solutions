from math import gcd
class Rational:
    def __init__(self, numer, denom):
        if numer == 0:
            denom = 1
        if denom < 0:
            numer = -1 * numer 
            denom = abs(denom)
        g = gcd(numer, denom)
        numer = numer / g
        denom = denom / g
        self.numer = numer
        self.denom = denom
        self.value = numer/denom 

    def __eq__(self, other):
        a1, b1 = self.numer, self.denom
        if isinstance(other, Rational):
            return a1 == other.numer and b1 == other.denom
        elif isinstance(other, float):  
            return (self.value) == other 

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        #(a₁ * b₂ + a₂ * b₁) / (b₁ * b₂)`.
        a1, b1 = self.numer, self.denom
        a2, b2 = other.numer, other.denom
        return (a1 * b2 + a2 * b1) / (b1 * b2)



    def __sub__(self, other):
        a1, b1 = self.numer, self.denom
        a2, b2 = other.numer, other.denom
        return (a1 * b2 - a2 * b1) / (b1 * b2)

    def __mul__(self, other):
        a1, b1 = self.numer, self.denom
        a2, b2 = other.numer, other.denom
        return (a1 * a2) / (b1 * b2)

    def __truediv__(self, other):
        a1, b1 = self.numer, self.denom
        a2, b2 = other.numer, other.denom
        return (a1 * b2) / (b1 * a2)

    def __abs__(self):
        return abs(self.numer) / abs(self.denom)

    def __pow__(self, power):
        return (self.numer ** power) / (self.denom ** power)

    def __rpow__(self, base):
        return (base ** self.numer) ** (1/ self.denom)
