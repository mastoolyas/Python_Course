class Fraction:
    def __init__(self, nom, denom):
        self._nom = nom
        self._denom = denom

    @staticmethod  # decorator from python that make the function available without declaring the class
    def from_string(string: str):  # therefor the function does not get self
        val = string.strip("/")
        return Fraction(int(val[0]), int(val[1]))

    def show_info(self):
        print(f"{self._nom}/{self._denom}")


# s = "3/5"
# f1 = Fraction.from_string(s)
f1 = Fraction(1,3)
f1.show_info()
