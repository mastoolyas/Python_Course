n1, n2 = 11, 3
res1 = n1 / n2   # result type float
print("{0} / {1} = {2:.3f}".format(n1, n2, res1)) # 11 / 3 = 3.666
print("{} / {} = {:.3f}".format(n1, n2, res1))    # 11 / 3 = 3.666
print(f"{n1} / {n2} = {res1:.3f}")                # 11 / 3 = 3.666 python > 3.6
n3 = "A"
print(f"{n3:<10}.") #A         .
print(f"{n3:>10}.") #         A.
print(f"{n3:^10}.") #    A     .

print(f"{n1:0x}") # b
print(f"{n1:0o}") # 13
print(f"{n1:0b}") # 1011




