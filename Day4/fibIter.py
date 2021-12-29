# 1 1 2 3 5 8 13 21 34 55 ...

class Fib:
    def __init__(self, cnt):
        self._cnt = cnt
        self._n1 = 1
        self._n2 = 1
        self._current = 0

    def __iter__(self):  # one iter for class, without it you can not run a loop on the class object
        return self

    def __next__(self):  # when declare iter have to declare next
        if self._current < self._cnt:
            self._current += 1
            if self._current <= 2:
                return 1
            else:
                n3 = self._n1 + self._n2
                self._n1, self._n2 = self._n2, n3
                return n3
        else:
            # done
            raise StopIteration()


# lst = [1,2,3]
fib10 = Fib(20)
# for n in fib10:  # dont save a list with all the fib arguments, calculate them one by one
#     print(n)     # can not run it more the once, current = cnt

iter_obj = fib10.__iter__()  # replace the for loop above
while True:
    try:
        n = next(iter_obj)
        print(n)
    except StopIteration:
        break

