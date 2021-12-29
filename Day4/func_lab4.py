from lab4 import logger, timer
import time


@logger
def duplicate_string(s: str) -> str:
    return s * 2


@logger  # to_upper = logger(to_upper)
def to_upper(s: str) -> str:
    return s.upper()


@logger
def first_last(s: str) -> str:
    return s[0] + s[-1] if len(s) > 0 else ""


@logger  # add = logger(add)
def add(n1: int, n2: int) -> int:
    return n1 + n2


def mult(n1: int, n2: int) -> int:
    return n1 * n2


def hello():
    print("hello")


@timer
def long_loop():
    for i in range(10_000_000):
        pass


@timer
def sleep_func(sec: int)-> int:
    time.sleep(sec)
    return sec



