glob_var = 9   # global var


def func():
    global glob_var  # only if you need to assign to a global var
    glob_var += 1
    var = 11.23  # local var
    print(f"in func: local var = {var}, global var = {glob_var}")
# function can not run with local and global var with the same name


print(f"main scope: global var = {glob_var}")
func()
