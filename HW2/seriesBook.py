import book


class book_series(book.Book):
    """
    #add 2 attributes: cnt, total
    # override: __init__ and __str__
    """
    def __init__(self, name: str, author: str, price: float, pages: int,
                 cnt: int, total: int):
        super().__init__(name, author, price, pages)  # bring the argum form the super (book)
        self.cnt = cnt
        self.total = total

    def __str__(self):
        return f"{super().__str__()} series count = {self.cnt} series total = {self.total}"

def main():
    sb1 = book_series(name="Lord of the rings", author="KK Tolkin", price=600, pages=789,
                    cnt=1, total=3)
    sb1.read(5)
    print(sb1)


if __name__ == "__main__": # main is the running app
    main()
