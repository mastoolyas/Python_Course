set1 = {1, 13, 8, 9, 1, 5, 1, 9, 22, 2, 8}  # set are key without value
print(set1)                                 # 1, 2, 5, 8, 9, 13, 22
set2 = {9, 1, 7, 10, 11, 11, 23}
print(set2)
set3 = set1.intersection(set2) # in both sets
print(set3)
set4 = set1.difference(set2) # without the in both sets
print(set4)
set5 = set1.symmetric_difference(set2) # same as XOR: set1 ^ set2
print(set5)
y = set()  # empty set
