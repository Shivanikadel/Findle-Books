import os
from reader import Reader
from user import User


class ReaderOperations:
    """This class is to operate the user role - Reader
    Methods:
    1. add_bookmark: it stores bookmarks in bookmark_list
    2. delete_bookmark: it deletes specific bookmark from bookmark_list
    3. save_favorite_book: it saves a book in favourite_book_list
    4. delete_favorite_book:  it deletes a book in favourite_book_list
    5. show_all_bookmarks: it shows list of all bookmarks added
    6. show_all_favorite_books: it shows list of all fav books
    """

    def add_bookmark(self, book_title, page_no, reader):
        """
        A method to add a bookmark,
        Attributes:
        book_title - it takes title name
        page_no - book page no
        bookmark_list - it takes in (book_title and page_no) and adds(append) to itself in list
        reader - intialising reader class

        """
        if len(book_title) == 0 or page_no =='':
            print("Enter a valid book title and page no.")
        elif len(book_title) == 0 or int(page_no) == 0:
            print("Enter a valid book title and page no.")
        else:
            if (book_title, page_no) not in reader.bookmark_list:
                reader.bookmark_list.append((book_title, page_no))
                print(reader.bookmark_list)

    # delete bookmark
    def delete_bookmark(self, num, reader):
        """
        A method to delete bookmark
        Attributes:
        num  - it is sequence number for bookmark from bookmark list starting from 1

        """
        if len(reader.bookmark_list):
            # check if num is valid

            if num == '':
                print("Enter Valid Number")
            if 0 < num <= int(len(reader.bookmark_list)):
                reader.bookmark_list.pop(num - 1)
                print(reader.bookmark_list)
                print("Bookmark removed Successfully!")
        else:
            print("No Bookmarks")

    def save_favorite_book(self, book_title, reader):
        """A method to save a fav book
        Attributes:
        book_title - it takes title name
        reader  - to initialise reader
        return: fav book in the list/ Already exists
        """
        if len(book_title) == 0:
            print("*Please Enter a Book Title")
        #checking if book_title is already in fav book list
        elif book_title not in reader.favourite_book_list:
            reader.favourite_book_list.append(book_title)
            print(reader.favourite_book_list)
        else:
            print("Already added")

    # delete favorite book
    def delete_favorite_book(self, num_or_title, reader):
        """
        A method to delete fav book
        :param num_or_title: it is sequence number or title of book from bookmark list
        :param reader: it initialises reader
        :return: deletes fav book
        """
        if isinstance(num_or_title, int):
            # check if num is valid
            if 0 < num_or_title <= len(reader.favourite_book_list):
                reader.favourite_book_list.pop(num_or_title - 1)
                print("Deleted favorite book by number Successfully")
            else:
                print("Book is not present in favorite books")
        elif isinstance(num_or_title, str):
            if num_or_title in reader.favourite_book_list:
                reader.favourite_book_list.remove(num_or_title)
                print("Deleted favorite book by name Successfully")
            else:
                print("Book is not present in favorite books")


    # show all favorite books and row numbers
    def show_all_favorite_books(self, reader):
        """
        A method to display all fav books
        :param reader: initialises reader
        :return:displays all fav book in the fav book list
        """
        #checks if the fav book list has anything
        if len(reader.favourite_book_list) == 0:
            print("No Favourite booklist")
        else:
            for i, book in enumerate(reader.favourite_book_list):
                print(f"{i + 1} {book}")

    # show all bookmarks and row numbers
    def show_all_bookmarks(self,reader):
        """
        A method to display all bookmarks
        :param reader: initialises reader
        :return: displays all bookmarks present in bookmark list
        """
        #checking if any bookmark in the bookmark list
        if len(reader.bookmark_list) == 0:
            print("NO Bookmarks")
        else:
            for i, bookmark in enumerate(reader.bookmark_list):
                print(f"{i + 1} {bookmark}")
