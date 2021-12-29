lst = ["a", "b", "c"]
tpl = (1, 22, 33, 444, 5, 6, 7, 8)
s = " , ".join(str(item) for item in tpl)
print(s)
