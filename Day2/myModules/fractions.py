from __future__ import annotations  # add type that was not define yet


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("both numerator and denominator must be int type")

        if denominator == 0:
            raise ZeroDivisionError("denominator cant be zero")

        self._numerator = numerator
        self._denominator = denominator

    def __str__(self):     # print/cast to print/add to string
        if self._numerator < self._denominator:  # 2, 5 => 2/5
            return f"{self._numerator}/{self._denominator}"
        elif self._numerator % self._denominator == 0:  # 15,5 => 3
            return f"{self._numerator // self._denominator}"
        else:  # 7,5 => 1 2/5
            return f"{self._numerator // self._denominator} " \
                f"{self._numerator % self._denominator}/{self._denominator}"

    def __float__(self) -> float:
        return self._numerator / self._denominator

    def __lt__(self, other: Fraction):
        if not isinstance(other, Fraction):
            raise TypeError(f"'<' not supported between instances of 'Fraction' and {type(other)}")
        return float(self) < float(other)

    def __add__(self, other: Fraction) -> Fraction:  # replace the + function
        return Fraction(self._denominator * other._numerator + other._denominator * self._numerator,
                        self._denominator * other._denominator)


fr1 = Fraction(20, 5)
fr2 = Fraction(3, 7)
print(fr1 > fr2)  # go to __it__ and __float__
print(fr1 + fr2)  # go to __str__ and __add__
