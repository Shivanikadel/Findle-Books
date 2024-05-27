import random

class User:
    """
    This class is used to represent User
    methods:
    init - it initialises the user attributes
    str -  returns a formatted string of User attributes
    """
    # initializing to represent class objects as string

    """
    -> init Method:
    param: user_id - It is user unique identification
    param: user_name - user's name for login
    param: user_password - user's password for login
    param: user_role - it is default in this application as reader
    
    """
    def __init__(self, user_id , user_name = "ricky.singh", user_password = "ricky45",
                 user_role = "reader"):
        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password
        self.user_role = user_role


    def __str__(self):
        """
        no param, just takes attributes from init
        Returns - formatted string of user attribute
        -------

        """
        formatted_str = str(self.user_id) + ";;;" + self.user_name + ";;;" + self.user_password + ";;;" + self.user_role
        return formatted_str


