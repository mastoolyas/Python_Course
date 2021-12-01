# ============== 1 =================
lst = [123, 456778, 5678]
lst_res = [f"{val}, {str(val)[::-1]}" for val in lst]
print("============== 1 =================")
print(lst_res)

# ============= 2 ===================
lst3 = [[1, 2, 3], [4], [5, 6, 7, 8, 9]] # defined list of lists
flat_list1 = [item for in_lst in lst3 for item in in_lst]
print("============== 2 =================")
print(flat_list1)

# ============= 3 =====================
s = "lmcalecmleamvjbihrbr;alvjrobjroshboarjbroakkbkaprkbvrvkl"
# 1. count each char in given string
d = {}
lst1 = [val for val in s]
for k in lst1:
    if k in d.keys():
        d[k] = d[k] + 1
    else:
        d[k] = 1
print("============== 3.1 =================")
print(d)

# 2. build reverse (key <-> value) dic.
d_rev = {}
for k1, v1 in d.items():
    if v1 in d_rev.keys():
        d_rev[v1].append(k1)
    else:
        d_rev[v1] = [k1]

print("============== 3.2 =================")
print(d_rev)