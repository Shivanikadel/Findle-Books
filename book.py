
class Book:
    """
    A class is used to represent Book
    Attributes:
        title: str
        str is to store the title
        author:str
        str is used to store the author
        release date: str
        str is used to store the release date
        last_update_date:str
        str is to store last update date
        language : str
        str to store language
        producer: str
        str to store producer
        book_path : str
        str to store path of the file
     Methods
    -------
    str method
     returns a formatted string of book attributes

    """
    def __init__(self, title="Alice’s Adventures in Wonderland", author="Lewis Carroll",
                 release_date="January, 1991", last_update_date="October 12, 2020", language="English",
                 producer="Arthur DiBianca and David Widger",
                 book_path= './data/books_data/1400-0.txt'):
        self.title = title
        self.author = author
        self.release_date = release_date
        self.last_update_date = last_update_date
        self.language = language
        self.producer = producer
        self.book_path = book_path

    def __str__(self):
        """
        returns a string of formatted details of the book.

        """
        formatted_str = self.title + ";;;" + self.author + ";;;" + self.release_date + ";;;" + self.last_update_date + ";;;" + self.language + ";;;" + self.producer + ";;;" + self.book_path
        return formatted_str


