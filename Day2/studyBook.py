import book


class StudyBook(book.Book):   # Inaternt from book
    def __init__(self, name: str, author: str, price: float, pages: int,
                 target_audience: str, include_exercise: bool):
        super().__init__(name, author, price, pages)  # bring the argum form the super (book)
        self.tar = target_audience
        self._exer = include_exercise

    def __str__(self):
        return f"{super().__str__()} target_audience = {self.tar}"


def main():
    sb1 = StudyBook(name="Python for beginners", author="Katia", price=600, pages=789,
                    target_audience="School, 9th grade", include_exercise=True)
    sb1.read(5)
    print(sb1)


if __name__ == "__main__": # main is the running app
    main()
