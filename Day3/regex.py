import re

# s = "a656KLGkh78o5toilg79%^%#W#@$%^@#$%@$#WE^JGCaaaa875a"
# mo = re.search("^a", s)
# mo = re.search("^a.*a$", s)
# s1 = "aaannnREFGHKHkjgkjKJGJHFGfFSRWQERTYUILOKJHGFFCVB"
# mo = re.search("^[a-zA-Z]+$", s1)
# if mo:
#     print("match")

# s = "abcabcabcabcabc"
# mo = re.search("^(abc){6}$", s)
# if mo:
#     print("match")

# s = "2/12/2021"
# mo = re.search(r"^(\d\d?)/(\d\d?)/(\d{4})$", s)
# if mo:
#     print(f"day: {mo.group(1)} at indexes: {mo.start(1)}-{mo.end(1)}")
#     print(f"month: {mo.group(2)} at indexes: {mo.start(2)}-{mo.end(2)}")
#     print(f"year: {mo.group(3)} at indexes: {mo.start(3)}-{mo.end(3)}")

 # 0
 # 1
 # 2
 # 14
 # 23
 # 42
 # "\d|[1-3]\d|4[12]"
tel = "03-61766699"
mo = re.search(r"^(0[23489])[ -]?(\d{7})$", tel)
if mo:
    print(f"prefix: {mo.group(1)}")
    print(f"tel: {mo.group(2)}")


