from user import User
import random


class UserOperation:
    """
    Useroperation has method used by the user while accessing the books
    Attributes
    ---------
    user_info_path:
    to store the related users
    user_info_list: list
    to store user info and use it in operations
    Methods
    ------
    load_user_info:
    it loads user info from txt to list
    user_registration
    allows user to register
    user_login
    authenticates user login
    write_user_info
    writes user info to list
    """
    user_info_path = "./data/result_data/users.txt"
    user_info_list = []

    # loading the user information
    def load_user_info(self):
        # opens the text file and write all the info to the list
        try:
            with open(UserOperation.user_info_path, 'r', encoding="utf8") as file:
                for lines in file:
                    if lines != '\n':
                        UserOperation.user_info_list.append(lines)
                # printing user information list
                # handling all types of exceptions
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
            return False
        except FileNotFoundError:
            print("File not found!!")
            return False
        except Exception as err:
            print(f"Unexpected error while opening is", repr(err))
            return False
        else:
            print("Loaded user info successfully")
            return True

    # registering users
    def user_registration(self, user_name, user_password, user_role="Reader"):
        user_name_list = []
        # random number generated for user id

        user_id_generator = random.randint(1000000000, 9999999999)
        for each in UserOperation.user_info_list:
            new_line = each.split(";;;")
            user_name_list.append(new_line[1])

            # checking if the user still exists
        if user_name in user_name_list:
            return False
            # formatting string to load user info to store in list
        else:

            formatted_newuser = str(user_id_generator) + ";;;" + user_name + ";;;" + user_password + ";;;" + user_role
            UserOperation.user_info_list.append(formatted_newuser)
            print("Registered Successfully")
            return True

    def user_login(self, user_name, user_password):
        # asking user to give user name password
        # prints success or not
        user_found = False
        for each in UserOperation.user_info_list:
            new_line = each.split(";;;")
            if user_name == new_line[1] and user_password == new_line[2]:
                print("login Successful")
                user_found = True
                return True

        if not user_found:
            print("The Login was unsuccessful . Please try again")
            return False

    # writing users information
    def write_user_info(self):
        # writing the user info to the list after registration
        try:
            with open(UserOperation.user_info_path, 'w', encoding="utf8") as file:
                for each in UserOperation.user_info_list:
                    each.strip()
                    file.write(each)
                    file.write('\n')
                print("Updated user info")
            return True
        except Exception as e:
            print("Error has occurred, e")
            return False

