def change_value(num: int):
    num = 4  # can not assign to integer


def change_list(l1):
    if not isinstance(l1, list):
        raise TypeError("Need to get list")
    l1.append(5)
    l1[0] = 100


def func():
    n = 11
    change_value(n)
    print(n)    # n =11
    lst = [1, 2, 3]
    change_list(lst)
    print(lst)   # list is immutable there for you can change it


def get_min_max_aver(lst: list):
    min_val = min(lst)
    max_val = max(lst)
    aver = sum(lst)/len(lst)

    return min_val, max_val, aver  # returning more then 1 value, it returns it as tuple


func()
lst = [1, 19, -5, 61, 52, 26, 9]
min1, max2, aver3 = get_min_max_aver(lst)
print(min1, max2, aver3)
