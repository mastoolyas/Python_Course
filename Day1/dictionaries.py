d = {"aa": 123, "bb": -15, "ccc": 92} # key: value, the order of the data is random
# key could not be: list, set or dic.
# key can be any kind of number, string, tuples
d["foo"] = 53     # add new, no key "foo" in d
d["bb"] = 6       # update key "bb" with 6
print(d)

# values access
key = "aa"
if key in d.keys():
    value = d[key]
    print(value)

value = d.get(key, -1)    # -1 is default
print(value)

# iterations on dictionary
for k in d.keys():
    print (k, d[k])

for v in d.values():
    print(v)

for k, v in d.items():
    print(k, v)
