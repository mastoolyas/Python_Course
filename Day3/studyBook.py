import book


class StudyBook(book.Book):
    def __init__(self, name: str, author: str, price: float, pages: int, target_audience: str, include_exercise: bool):
        super().__init__(name, author, price, pages)
        self._target_audience = target_audience
        self._include_exercise = include_exercise

    def __str__(self):
        return f"{super().__str__()} target_audience = {self._target_audience}"


def main():
    sb1 = StudyBook("python for beginners", "someone smart", 600, 789, "school, 9th grade", True)
    sb1.read(5)
    print(sb1)


if __name__ == '__main__':
    main()
