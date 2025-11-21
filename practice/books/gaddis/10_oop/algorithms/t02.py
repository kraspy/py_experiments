class Book:
    def __init__(
        self,
        title: str,
        author: str,
        publisher: str,
    ) -> None:
        self.__title = title
        self.__author = author
        self.__publisher = publisher

    def get_title(self):
        return self.__title

    def set_title(self, value):
        self.__title = value

    def get_author(self):
        return self.__author

    def set_author(self, value):
        self.__author = value

    def get_publisher(self):
        return self.__publisher

    def set_publisher(self, value):
        self.__publisher = value

    title = property(get_title, set_title)
    author = property(get_author, set_author)
    publisher = property(get_publisher, set_publisher)

    def __str__(self) -> str:
        return f'{self.__title}'


book = Book('Book title #1', 'Alex Miles', 'Alpina book')

print(book)
