import time


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


class MatchingObject:
    def __init__(self, start_index: int, end_index: int, match_count: int):
        self._start_index = start_index
        self._end_index = end_index
        self._match_count = match_count

    def __str__(self):
        return f"match #{self._match_count} at {self._start_index}-{self._end_index}"

def sub_strings_matcher(s: str, sub: str, to_overlap=True):
    """
        write iterator/generator to find all matches of
        sub-string in given string - ONE by ONE
    :param s: string to search into
    :param sub: string to search
    :param to_overlap: to allowed overlapping
    :return: iterator of all matches(one by one)
    """
    print("!!!!")
    gap = 1 if to_overlap else len(sub)
    cnt = 1
    ind = s.find(sub)
    while ind != -1:
        yield MatchingObject(ind, ind+len(sub), cnt)  # generator function, return will end the function
        ind = s.find(sub, ind + gap)
        cnt += 1



s = "74754 aaa ljkaa aa aaaaaaaa foo"
sub = "aa"
all_matches = sub_strings_matcher(s, sub, True)

for mo in all_matches:         # the generator function will start only when the for start
    print(mo)
