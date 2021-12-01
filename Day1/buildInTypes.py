import math

flag = False       # bool
print(type(flag))

val = None         # NoneType
print(type(val))

num1 = 5467        # int
print(type(num1))

num2 = 54.67       # float
print(type(num2))

num3 = -11 + 5j    # complex
print(type(num3))

n1, n2 = 11, 3
res1 = n1 / n2   # result type float
res2 = n1 // n2  # casting to int
print(res1, res2**3)
n1 -= 3          # n1 = n1 -3 *= += /=
n2 = "abc"
n1, n2 = n2, n1*10 #swap
print(n1, n2)
n1 = 50
res1 = math.hypot(n1, n2)  # Pitaguras
help(math.radians)
print(res1)



