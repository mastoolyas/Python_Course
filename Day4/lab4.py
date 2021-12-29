import func_lab4


def logger(old_func):
    def new_func(*args):
        print(f"LOG: in func: {old_func.__name__}, params = {args}")
        res = old_func(*args)
        print(f"LOG: out func: {old_func.__name__}, params = {args} calc res = {res}")
        return res

    return new_func


def timer(old_func):
    def new_func(*args):
        start_time = time.time()
        res = old_func(*args)
        end_time = time.time()
        print(f"total duration of func: {old_func.__name__} is {end_time-start_time}")
        return res

    return new_func
