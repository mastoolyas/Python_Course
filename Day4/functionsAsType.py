from typing import Callable
# function is a type

def duplicate_string(s: str) -> str:
    return s * 2


def to_upper(s: str) -> str:
    return s.upper()


def first_last(s: str) -> str:
    return s[0] + s[-1] if len(s) > 0 else ""


# Callable is setting that the func get str and output str (bat not testing)
def func(callback_func: Callable[[str], str], string: str):  # callback_func is function (s:str) -> str
    s = "python"
    res_str = callback_func(string)  # invoke
    print(res_str)


def func1() -> Callable[[str], str]:
    return lambda s: s[::-1]  # function can return a function, and it gets the outer function parameters


def func2(num: int):
    def inner():
        print(num+10)  # and it gets the outer function parameters
    return inner

# func(duplicate_string, "foo")
# func(to_upper, "hello")
funchandl = func1()
print(funchandl("lalala"))
inner_3 = func2(3)
inner_11 = func2(11)
inner_11()
inner_3()

