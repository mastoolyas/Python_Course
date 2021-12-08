import datetime


class Book:
    def __init__(self, name, author, price, pages):  # constructor run for every book instance
    # first argum is allways the class itself never mind the name
        self._name = name
        self._author = author
        self.price = price
        self._num_of_pages = pages   # data member is always in self
        self._current_page = 1
        self._date = datetime.date

    def read(self, pages_to_read=10):
        self._current_page = min(self._num_of_pages,
                                 self._current_page + pages_to_read)  # if num of pages is not over add pages to read to it

    def __str__(self):  # to string, build and return string, does not print it
        return f"name = {self._name}, price = {self.price}, " \
            f"pages = {self._current_page}/{self._num_of_pages}"


def main():
    b1 = Book("foo", "foo1", 123.90, 307)
    b2 = Book("bar", "bar1", 89.50, 444)
    b2.read(15)  # read(b2, 15)
    b2.read()
    # print(b2)
    s = str(b2)
    # print(s)
    print(f"b2: {b2}")


# main space code
if __name__ == "__main__": # main is the running app
    main()



