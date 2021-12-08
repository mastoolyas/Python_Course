def ex1():
    s = "ajbkjbcdljdb clndlckandc klsjcnk"
    n = input("Enter Number")

    while not n.isnumeric():
        n = input("Enter Number")
    n = int(n)
    lst = [s[i:i+n] for i in range(0, len(s), n)]
    print(lst)


def ex2():
    lst = [11, 7, 19, 8, 2]
    lst_res = ["*" * num for num in lst]
    print(lst_res)


def ex3():
    lst1 = ['a', 'b', 'c', 'd']
    lst2 = ['1', '2', '3', '4']
    lst = [lst1[i] + lst2[-i - 1] for i in range(len(lst1))]
    print(lst)


def ex4():
    d = {}
    val = input("enter value, -1 to stop: ")
    while val != "-1":
        d[val] = d.get(val, 0) + 1
        val = input("enter value, -1 to stop: ")
    print(d)
    max_tpl = (None,0) # max value, max count
    second_max_tpl = (None, 0)  # max value, max count
    for item, cnt in d.items():
       if cnt > max_tpl[1]:
            second_max_tpl = max_tpl
            max_tpl = (item, cnt)
       elif cnt > second_max_tpl[1]:
            second_max_tpl = (item, cnt)
    print("Mxx is: ", max_tpl)
    print("Sec. max is: ", second_max_tpl)


ex1()
ex2()
ex3()
ex4()

