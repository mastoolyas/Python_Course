import re


def ex1():
    reg_ex = re.compile(r"^[-+]?\d+(\.\d+)?(e[-+]?\d+)?$", re.I)
    with open("numbers.txt", "r") as fo:
        for line in fo:
            if reg_ex.search(line):
                print(line.strip())


def ex2():
    s = "hello         all, one two  three,python,  aaa      bbb    "
    #1. split by ','
    sub_strings = [sub.strip() for sub in s.split(",")]
    # print(sub_strings)

    reg_ex = re.compile(r"^(\w+)\s+(\w+)$")
    #2. filter only 2-words sub strings
    two_words_seq = filter(lambda sub: reg_ex.search(sub), sub_strings)
    # print(list(two_words_seq))
    #3. swap words in remained sub-strings
    # result: ["all hello", "bbb aaa"] use lambda functions, filter and map
    swap_order_seq = map(lambda string: reg_ex.sub(r"\2 \1", string), two_words_seq)
    print(list(swap_order_seq))

ex2()