#
#
# # __doc__ """ ... """
# # default values can be only from the last inputs num2: int = 0
# def add(num1: int, num2: int = 0) -> int:
#     """
#     for example: add(2, 3) -> 5
#     :param num1: integer value
#     :param num2: integer value
#     :return: sum of num1 and num2
#     """
#     res = num1 + num2
#     return res
#
#
#
# def add2(num1: int, num2: int = 6, num3: int = 0) -> int:
#     """
#
#     :param num1:
#     :param num2:
#     :param num3:
#     :return:
#     """
#
#     if not isinstance(num1, int):
#         raise TypeError("num1 must be int")
#     if not isinstance(num2, int):
#         raise TypeError("num2 must be int")
#     if not isinstance(num3, int):
#         raise TypeError("num3 must be int")
#     return num1 + num2 + num3
#
#
# print(add2("aa", "bb", "cc")) # get error num3 must be int
#
# # flexible parameters in a function
# print(add(num1=2)) # can send a value for a name parameter, not in order


def func(*values):
    print(values)


def func1(s1, s2, s3, s4, s5, s6):
    print(s1, s2, s3, s4, s5, s6)


def func2(**kwargs):   # ** need to send args with names
    print(kwargs)


s = "a,b,c,d,e,f"
lst = s.split(",")  # split s by ,
s1 = "Python"
func1(*s1)           # str is a tpl of chars
func1(*lst)

func2(name="Katia", lastname="Barak", ID=123456789)
func()
func(4, "UU", 9.7, [1, 2, 3], (4, 5))
