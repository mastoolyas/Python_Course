import time

import decorators as dec

@dec.timer
@dec.logger
def duplicate_string(s: str) -> str:
    return s * 2


@dec.timer
@dec.logger  # Decorator enable, to_upper = logger(to_upper)
def to_upper(s: str) -> str:
    return s.upper()


@dec.timer
@dec.logger
def first_last(s: str) -> str:
    return s[0] + s[-1] if len(s) > 0 else ""


@dec.timer
@dec.logger
def add(n1: int, n2: int) -> int:
    return n1+n2


@dec.timer
@dec.logger
def mult(n1: int, n2: int) -> int:
    return n1*n2


@dec.timer
@dec.logger
def hello():
    print("hello")


@dec.timer("MS")
def sleep_func(sec: int):
    time.sleep(sec)
