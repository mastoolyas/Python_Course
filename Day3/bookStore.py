from book import Book
from studyBook import StudyBook


class BookStore:
    def __init__(self, name):
        self._name = name
        self._booksCollection = [] # list for Book and StudyBook items

    def add(self, new_book: Book):
        """

        :param new_book: Must be Book type or derived from Book types
        :return: None
        """
        if isinstance(new_book, Book):
            self._booksCollection.append(new_book)
        else:
            raise TypeError("only Book and derived types of Book are allowed")

    def __str__(self):
        title = f" =========== {self._name} ============\n"
        # for b in self._booksCollection:
        #     s += str(b) + "\n"
        s1 = title + "\n".join(str(b) for b in self._booksCollection)

        return s1
        

    def __len__(self):
        return len(self._booksCollection)

    def __contains__(self, item):
        return item in self._booksCollection

    def sort_books(self):
        self._booksCollection.sort()


def main():
    b1 = Book("foo", "foo1", 123.90, 307)
    b2 = Book("bar", "bar1", 89.50, 444)
    sb1 = StudyBook("python for beginners", "someone smart", 600, 789, "school, 9th grade", True)

    bs = BookStore("IAI Book Store")
    bs.add(b1)
    bs.add(sb1)
    bs.add(b2)
    print(bs)
    # print(len(bs))
    # if b1 in bs:
    #     print("in")
    # bs.sort_books()
    # print(bs)


if __name__ == '__main__':
    main()





