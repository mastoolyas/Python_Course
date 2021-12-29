import math


def factorial(num):
    x = 1
    for i in range(1, num+1):
        x *= i
    return x

#
# fh = lambda num: num ** 2
#
# # print(type(fh))
# print(fh(5))


def grater_than_15(num: int):
    return num > 15


def main():
    lst = [2, 14, 53, 22, -10, 95, 70, 19, 7]
    # # odds = []
    # # for val in lst:
    # #     if val % 2:
    # #         odds.append(val)
    # # res = filter(grater_than_15, lst)
    # res = filter(lambda num: num % 2 == 0, lst)
    # lst.append(30)
    # # lst_res = list(res)
    # # print(lst_res)
    # for r in res:
    #     print(r)
    #
    # print(sum(res))

    res = filter(lambda num: num + 10, lst) #2 14 53 22 95 70 19 7
    res = map(lambda num: num + 10, lst)    #12 24 63 32 0 105 80 29 17

    res = filter(lambda num: num > 15, lst)  # 53 22 95 70 19
    res = map(lambda num: num > 15, lst)  # False False True True False True True True False

    for x in res:
        print(x, end=" ")


if __name__ == '__main__':
    main()