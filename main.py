
import os
import re
import random
from book import Book
from book_operation import BookOperation
from user import User
from reader_operation import ReaderOperations
from reader import Reader
from user_operation import UserOperation
user_obj = UserOperation()
bookop_obj = BookOperation()
reader_obj = ReaderOperations()
"""
user_obj os calling UserOperation()
book_obj is calling BookOperation()
reader_obj is calling ReaderOperation()
"""
def menu_display():
    """
    This method is to display menu of the main
    """
    print('Welcome to Findle - Your Ebook Reading Application')
    print('[1] Login')
    print('[2] Register')
    print('[3] Display Book Title')
    print('[4] Search Books by Author')
    print('[5] Exit the Application')
def app_menu():
    """
    This method is for application menu for main
    """
    print("You are now in accessing the Application Menu")
    print('[1] Access Book Titles available')
    print('[2] Access content of a Book')
    print('[3] Read Book Pages ')
    print('[4] Show number of Book classified by Year')
    print('[5] Show Book Lines,Words and Chapter Information')
    print('[6] Show all the Bookmarks')
    print('[7] Show all the Favourite Books')
    print('[8] Add a Bookmark')
    print('[9] Add a Favourite Book')
    print('[10] Delete a Bookmark')
    print('[11] Delete a Favourite Book')
    print('[12] Access Books by Author')
    print('[13] Logout')

def app_menu_selections():
    reader = Reader()
    """
    This method is for application menu selection 
    where input from the user is taken from user 
    """
    while True:
        #calling app_menu method
        app_menu()
        app_selection = input("Enter the selection from Application menu: ")
        #extracting and loading info
        bookop_obj.extract_book_info()
        bookop_obj.load_book_info()

        #checking input for app_selection is digit or not
        while not app_selection.isdigit():
            print('Input valid number between 1-12')
            app_selection = input("Choose from the app menu to get started: ")
        else:
            while app_selection not in ['1','2','3','4','5','6','7','8','9','10','11','12','13']:
                print("You have entered a wrong choice")
                app_selection = input("Choose from the Application menu to get started: ")
        app_selection = int(app_selection)

        #the option 1 where user access the titles, we call display_titles here
        if app_selection == 1:
            print('---You are viewing the Titles now---')
            page_input = input("Enter the Page number: ")
            #checking input
            while not str(page_input).isdigit():
                print("You have entered invalid input, enter page no. in digit")
                page_input = input("Enter the Page number: ")
            else:
                if int(page_input) > 0:
                    page_input = int(page_input)
                    bookop_obj.display_titles(page_input)
                else:
                    print("Enter a number greater than zero")
                    page_input = input("Enter the Page number: ")
                    page_input = int(page_input)
                    bookop_obj.display_titles(page_input)
        #option 2 is for book content, we call shw_book_content here
        elif app_selection == 2:
            print('---You are accessing the book content---')
            get_title = input("Please enter the Title: ")
            bookop_obj.show_book_content(get_title)
        #option 3 is to show book pages, we all display_data here
        elif app_selection == 3:
            print('--Show Book Pages--')
            dis_title = input("Please enter Title of a Book: ")
            dis_pgno = input("Please enter the page no. you want to access: ")
            #validating input
            if dis_pgno == '':
                print("Invalid Page Number")
            else:
                dis_pgno = int(dis_pgno)
                bookop_obj.display_data(dis_title.strip(),dis_pgno)
        # option 4 is for displaying books released year, we call get_book_release_year here
        elif app_selection == 4:
            print('--Show number of Book classified by Year--')
            bookop_obj.get_book_release_year()
        # option 5 is for book info, lines, words, we call get_counts here
        elif app_selection == 5:
            print('--Show Book Lines,Words and Chapter Information--')
            bk_title = input("Enter the Book Title for info: ")
            c = bookop_obj.get_counts(bk_title)
            print(c)
        # option 6 is for display list of all bookmarks, we call show_all_bookmarks here
        elif app_selection == 6:
            print('--Show all Bookmark--')
            reader_obj.show_all_bookmarks(reader)
        # option 7 is for displaying list of all fav books, we call show_all_favorite_books here
        elif app_selection == 7:
            print('--Show all favourite Books--')
            reader_obj.show_all_favorite_books(reader)
        # option 8 is for adding a bookmark, we call add_bookmark here
        elif app_selection == 8:
            print('--Add a Bookmark--')
            add_bk_title = input("Enter book Title of your bookmark: ")
            add_pg_no = input("Enter page no. for bookmark: ")
            reader_obj.add_bookmark(add_bk_title, add_pg_no, reader)
        # option 9 is for saving a fav book, we call save_favorite_book here
        elif app_selection == 9:
            print('--Save a favourite Book-- ')
            add_bk_title = input("Enter Book Title of your Favourite book: ")
            reader_obj.save_favorite_book(add_bk_title,reader)
        #option 10 is for deleting a bookmark, we call delete_bookmark here
        elif app_selection == 10:
            print('--Delete a Bookmark--')
            reader_obj.show_all_bookmarks(reader)
            del_pgno = input("Enter the sequence no. of Bookmark from list: ")
            while not str(del_pgno).isdigit():
                print("you have entered invalid input, enter page no. in digit")
                del_pgno = int(input("Enter sequence no. for bookmark from list: "))
            else:
                reader_obj.delete_bookmark(int(del_pgno),reader)
        #option 11 is for deliting fav book we call, delete_favorite_book here
        elif app_selection == 11:
            print('--Delete a favourite Book--')
            reader_obj.show_all_favorite_books(reader)
            print("Please select the input type")
            print('[1] Book Title ')
            print('[2] Sequence number of favourite Book')
            pick = input("Selection:")
            if pick == '1':
                del_favbk = input("Enter favourite book title: ")
                if del_favbk == '':
                    print("Please enter a valid title")
                else:
                    reader_obj.delete_favorite_book(del_favbk, reader)
            elif pick == '2':
                del_favbk = input("Sequence no. from favourite Book: ")
                if del_favbk == '':
                    print("Enter a valid sequence number")
                else:
                    while not str(del_favbk).isdigit():
                        print("you have entered invalid input, enter sequence no. in digit")
                        del_favbk = input("Enter page no. for bookmark: ")
                    del_favbk = int(del_favbk)
                    reader_obj.delete_favorite_book(del_favbk, reader)
            else:
                print("Invalid selection , enter 1 or 2")

        #option 12 is for getting books by author, we call get_book_by_author here
        elif app_selection == 12:
            print("--Search Books by Author Name--")
            get_author = input("Enter Author name: ")
            bookop_obj.get_book_by_author(get_author)
        #option 13 is to exit app menu
        elif app_selection == 13:
            print('--Exiting the App Menu--')
            break
        else:
            print("Oops! Invalid Selection")
            break

def main():
    """
    This method is for calling all the methods
    in the application to run the program

    gives output as user inputs
    -------

    """
    while True:
        user_obj.load_user_info()
        bookop_obj.extract_book_info()
        bookop_obj.load_book_info()
        menu_display()
        selection = input("Enter your selection: ")
        while not selection.isdigit():
            print('Input valid number between 1-5: ')
            selection = input("Choose from the menu to get started: ")
        else:
            while selection not in ['1','2','3','4','5']:
                print("you have entered a wrong choice")
                selection = input("Choose from the menu to get started: ")
        selection = int(selection)
        #option 1 is for user login, we call user_login here
        if selection == 1:
            print("Please enter your user name and password to login")
            user_name = input('please enter user name: ')
            user_password = input('please enter password: ')
            check = user_obj.user_login(user_name, user_password)
            if check:
                app_menu_selections()
            else:
                print("User Id and Password doesn't exist, try login or Register")
        #option 2 is for user registration, we call user_registration here
        elif selection == 2:
            print("Hey there! Register Here ")
            regis_name = input("Register your username: ")
            regis_password = input("Set your password: ")
            reg_check = user_obj.user_registration(regis_name, regis_password)

            print(reg_check)
            if reg_check:
                user_obj.write_user_info()
            else:
                print("User already exists")
        #option 3 is for user to view titles, we call display_titles here
        elif selection == 3:
            print('---You are viewing the Titles now---')
            page_input = input("Enter the Page number: ")

            while not str(page_input).isdigit():
                print("you have entered invalid input, enter page no. in digit")
                page_input = input("Enter the Page number: ")
            else:
                if int(page_input) > 0 :
                    page_input = int(page_input)
                    bookop_obj.display_titles(page_input)
                else:
                    print("Enter a number greater than zero")
        #option 4 is to get titles by author, we call get_book_by_author here
        elif selection == 4:
            print("--Search Books by Author Name--")
            get_author = input("Enter Author name: ")
            bookop_obj.get_book_by_author(get_author)
        #option 5 is to exit from the program
        elif selection == 5:
            print("Exiting the Application")
            break
        else:
            print("Oops! Invalid Selection. ")
            break

if __name__ == '__main__':
    main()
