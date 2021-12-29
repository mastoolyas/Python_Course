# lst1 = [1, 2, 3, 4]
# lst2 = lst1               # list, set, dic, class is mutibale
#
# lst1[0] = 100
# print(lst2)
#
# print(lst1 == lst2)
# print(lst1 is lst2)

num1 = 10
num2 = 9
num2 += 1

print(num1 == num2)       # numbers are inmutibale (like all premities and tafes)
print(num1 is num2)       # true, compere the address

# int is pointer for a cell, and if there is a cell like this, both object will point to the same cell
# python does not promise to collect all pointers to the same cell if there are equal

num1 = 5
