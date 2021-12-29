from __future__ import annotations


class Book:
    def __init__(self, name: str, author: str, price: float, pages: int):
        self._name = name
        self._author = author
        self._price = price
        self._total_pages = pages
        self._current_page = 1

    def read(self, pages_to_read=10):
        self._current_page = min(self._total_pages,
                                 self._current_page + pages_to_read)

    def __str__(self):
        return f"name = {self._name}, price = {self._price}, " \
            f"pages = {self._current_page}/{self._total_pages}"

    def __lt__(self, other: Book):
        return self._price < other._price


def main():
    b1 = Book("foo", "foo1", 123.90, 307)
    b2 = Book("bar", "bar1", 89.50, 444)
    b2.read(15)  # read(b2, 15)
    b2.read()
    # print(b2)
    s = str(b2)
    # print(s)

    print(f"b2: {b2}")
    print(b1)


if __name__ == "__main__":
    main()
