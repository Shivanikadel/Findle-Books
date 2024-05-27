
from user import User
"""class reader is to support reader operations, and it needs user data
to store the changes of reader while adding and deleting bookmark,
saving and deleting favourite bookbook"""
class Reader(User):
    """creating init method which contains information about a reader,
    this will inherit the user class
    Parameters - user_id, user_name, user_password, user roll --> are string
    we have favourite_book_list and bookmark_list as list"""

    def __init__(self, user_id="123456789", user_name="xyz0001", user_password="sgfkj@4566", user_role="Reader",
                 favourite_book_list=[], bookmark_list=[]):
        # self represents the instance of the class, used to access the user_id, user_name, user_password, user_role, fav. book list and bookmarklist
        super().__init__(user_id, user_name, user_password, user_role)
        self.favourite_book_list = favourite_book_list
        self.bookmark_list = bookmark_list


    def __str__(self):
        # converting specified value to string

        return str(
            f"{self.user_id};;;{self.user_name};;;{self.user_password};;;{self.user_role};;;{self.favourite_book_list};;;{self.bookmark_list}")
         #returning formatted string for all the attributes of reader
