def add(*values):
    """
    recives any number of parameters
    :return: calc and return sum of numeric values only
    """
    sum1 = 0
    for i in values:
        if isinstance(i, (int, float, complex)):
            sum1 = i + sum1
    return sum1


print(add(10, 17, -3.3, "foo", [10, 20], "12", 5.5))
tpl = (11, 12, 13, 14)
print(add(*tpl))  # send to function1 tpl items one by one

