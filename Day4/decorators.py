import time


def logger(old_func):
    def new_func(*args):
        start_time = time.time()
        print(f"LOG: in func: {old_func.__name__}, params = {args}")
        res = old_func(*args)
        end_time = time.time()
        print(f"LOG: out func: {old_func.__name__}, params = {args} calc res = {res}")
        return res

    return new_func


def timer(units):
    def timer_decorator(old_func):
        def new_func(*params):
            start_time = time.time()
            return_val = old_func(*params)
            duration = time.time() - start_time
            if units == "MS":
                print(f"total duration of func: {old_func.__name__} is"
                      f" {duration * 1000:.3f} ms")
            elif units == "SEC":
                print(f"total duration of func: {old_func.__name__} is"
                      f" {duration:.3f} sec")
            elif units == "MIN":
                print(f"total duration of func: {old_func.__name__} is"
                      f" {duration / 60:.3f} min")
            return return_val

        return new_func

    return timer_decorator

