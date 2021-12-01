lst = [12, 3.7, "Python", [11, "bar", -2.8]]
print(lst[-1][1][0]) # b

lst1 = list(range(1, 31, 3))  # [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
lst1 = lst1 + [29, 30]        # [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 29, 30] not good
lst1.append(11)               # add one item to the end o(1)
lst1.extend([12, 13, 14])     # add more then one item to the end o(1)
#lst1 = lst1.pop(-2)           # remove the -2 (by index) item from the end 13
lst1.remove(13)               # remove the first item with value 13
print(lst1)
lst2 = [0] * 10               # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(4 in lst1)              # True
print(lst1[4::2])             # [16, 22, 28, 30, 12, 14]

for c in lst2:   # dont use index for print all items in list
    print(c, end=" ")  # 0 0 0 0 0 0 0 0 0 0

print()
# ========= list comprehension ===============
lst2 = [val + 10 for val in lst2]
print(lst2)

lst3 = [[1, 2, 3], [4], [5, 6, 7, 8, 9]]
lst4 = [sub_list[len(sub_list)//2] for sub_list in lst3]
print(lst4)
