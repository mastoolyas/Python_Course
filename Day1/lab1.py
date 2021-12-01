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
