#importing random library
import os
#importing re library
import re
#importing Book from book
from book import Book

class BookOperation:

    """
    A class to operate on books
    Attributes:
    ----------
    book_folder_path: str
    it stores the directory where it has all the books to work on
    book_info_path: str
    it stores where the information where book info is stored
    book_title-list : list
    a list to store all the book titles
    book_info_dict: dictionary
    it stores book titles and objects

    Methods:
    ------
    extra_book_info:
    extracts all the information from the book data
    load_book_info:
    loads book data to a list and dictionary
    get_counts:
    this method counts no of words, chapters and lines in a book
    display_title:
    this method displays titles of the book
    show_book_contents:
    it shows the content list of book
    show_book_text:
    it displays text from the book

    """
    book_folder_path = './data/books_data/'
    book_info_path = './data/result_data/books.txt'
    book_title_list = []
    book_info_dict = {}

    def extract_book_info(self):
        """
        A method to extracts all book information
        Attributes
        ---------
        book_path: str
        gives the path for the book
        title_name:str
        extracts title from book
        release_date_update:str
        specifies release date of the book
        last_update_date:str
        gives the last updated date
        language: str
        language of the book its written
        producer: str
        the producer of the book
        str_list: list
        to load the book attributes use it further

        """
        str_list = []
        try:
            #opening the books to get all the infomation
            for file in os.listdir(BookOperation.book_folder_path):
                book_path = BookOperation.book_folder_path + file
                title_name = ""
                author_name = ""
                release_date_update = ""
                last_update_date = ""
                language = ""
                producer = ""
                #comparing the bboks with specified attibutes
                with open(book_path, encoding="utf8") as individual_file:
                    raw_data = individual_file.readlines()

                    for line in raw_data:
                        each_line = line.strip()
                        #extract the information when it matches the keyword
                        result = re.search(r"Title:", each_line)
                        if result:
                            title_name = each_line.split(':', 1)[1]
                        if not title_name:
                            title_name = 'NONE'

                    for line in raw_data:
                        each_line = line.strip()
                        result = re.search(r'Author:', each_line)
                        if result:
                            author_name = each_line.split(':', 1)[1]
                        if not author_name:
                            author_name = 'NONE'

                    for line in raw_data:
                        each_line = line.strip()
                        result = re.search(r'Release Date:', each_line)
                        if result:
                            release_date = each_line.split(':', 1)[1]
                            release_date_update = release_date.split('[', 1)[0]
                        if not release_date_update:
                            release_date_update = 'NONE'

                    for line in raw_data:
                        each_line = line.strip()
                        search_words = ["Most recently updated:", "Last Updated:"]
                        for word in search_words:
                            if each_line.find(word) != -1:
                                last_update_date = each_line.split(':', 1)[1]
                                last_update_date = last_update_date.split(']', 1)[0]
                            if not last_update_date:
                                last_update_date = 'NONE'

                    for line in raw_data:
                        each_line = line.strip()
                        result = re.search(r'Language:', each_line)
                        if result:
                            language = each_line.split(':', 1)[1]
                        if not language:
                            language = 'NONE'

                    for line in raw_data:
                        each_line = line.strip()
                        result = re.search(r'Produced by:', each_line)
                        if result:
                            producer = each_line.split(':', 1)[1]
                        if not producer:
                            producer = 'NONE'

                # attaching all the extracted attributes into the final str
                final_str = title_name.strip() + ";;;" + author_name.strip() + ";;;" + release_date_update + ";;;" + last_update_date + ";;;" + language + ";;;" + producer + ";;;" + book_path

                if final_str not in str_list:
                    str_list.append(final_str)
                    # appending all the information to the books.txt
                with open(BookOperation.book_info_path, 'w', encoding="utf8") as file:
                    for l in str_list:
                        file.write(l)
                        file.write('\n')

            self.load_book_info()
        #handling the exceptions of file operations
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
            return True

    def load_book_info(self):
        """
        it loads all the information from the books.txt to boot title and book info dictionary
        Attributes
        --------
         new_line: str
         helps to store a line form file
         book_obj: object
         store book object
        """
        try:
            #opening file to read the data and load what neede
            with open(BookOperation.book_info_path, 'r', encoding="utf8") as file:
                new_line = []
                for each_line in file:
                    new_line = each_line.split(";;;")
                    BookOperation.book_title_list.append(new_line[0])
                    book_obj = Book(new_line[0], new_line[1], new_line[2], new_line[3], new_line[4], new_line[5],
                                    new_line[6])
                    BookOperation.book_info_dict[new_line[0]] = book_obj
        #handling error messages of book operations
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
            return True

    def get_counts(self, title):
        """
        This method gets the count of no of words, no of lines and chapter count
        Attributes
        ---------
        num_of_lines: int
        used to store lines of book
        str_line_no: list
        used to store the index of line in file
        num_of_words:list
        stores no.of words
        count_chapters:int
        count number of chapters
        chapter_list:list
        store chapter list
        total_num_of_words:int
        store totsl no of wors in a book

        """
        num_of_lines = 0
        str_line_no = []
        num_of_words = []
        count_chapter = 0
        chapter_list = []
        total_num_of_words = 0
        # checks if title is in title list
        if title.strip() in BookOperation.book_title_list:
            book_object = BookOperation.book_info_dict[title]
            book_path = book_object.book_path
            search_list = ['CHAPTER', 'Chapter']
            try:
               #reading books
                with open(book_path.strip(), 'r', encoding='utf-8') as f:
                    for l_no, line in enumerate(f):
                        new_line = line.strip()
                        result1 = re.findall(r'\*{3}\s[A-Z]', new_line)
                        if result1:
                            str_line_no.append(l_no)
                    num_of_lines = str_line_no[1] - str_line_no[0]
                #opening books for getting no of words in the file
                with open(book_path.strip(), 'r', encoding='utf-8') as fp:
                    for l_no, line in enumerate(fp):
                        if str_line_no[0] < l_no < str_line_no[1]:
                            new_data = line.strip()
                            new_string = re.sub(r'\—', ' ', new_data)
                            new_string = re.sub(r'[^\w\s]', '', new_string)
                            word_list = new_string.split()
                            number_of_words_eachline = len(word_list)
                            num_of_words.append(number_of_words_eachline)
                            l_no + 1
                    total_num_of_words = sum(num_of_words)
               #opening the books to get start and end of the book
                with open(book_path.strip(), 'r', encoding='utf-8') as f:
                    for l_no, line in enumerate(f):
                        new_line = line.strip()
                        result1 = re.findall(r'\*{3}\s[A-Z]', new_line)
                        if result1:
                            str_line_no.append(l_no)
                #getting chapter counts of the book
                with open(book_path.strip(), 'r', encoding='utf-8') as fp:
                    for l_no, line in enumerate(fp):
                        if str_line_no[0] < l_no < str_line_no[1]:
                            new_data = line.strip()
                            new_string = re.sub(r'[^\w\s]', '', new_data )
                            for word in search_list:
                                if word in new_string:
                                    chapter_list.append(new_string)
                    count_chapter = len(set(chapter_list))
                    if count_chapter == 0:
                        return num_of_lines, total_num_of_words, "NO CHAPTERS"
                #returns no of lines and words and chapters of the book
                return " No. of lines: " + str(num_of_lines)+ " Total no. of Words: "+str( total_num_of_words)+ " Total no. of Chapters: "+str (count_chapter)
            except Exception as e:
                print("Error has occurred:", e)
        else:
            print("NO CHAPTERS")


    def display_titles(self, page_num):
        """
        displays titles of the total books
        Arributes
        --------
        display_num : int
        show a the page number of the titles

        """

        try:
            if str(page_num).isdigit():
                display_num = 0
                if page_num == 1:
                    display_num = 1
                    print("----------------List of Book Titles--------------")
                    #prints book titles page according to the input
                    for each in BookOperation.book_title_list:
                        print(f"{display_num} {each}")
                        display_num += 1
                        if display_num > 10:
                            break
                    print("Current Page : 1")
                    print("Total Pages : 10")
                    print("--------------------The End----------------------")
                if page_num == 2:
                    display_num = 11
                    print("----------------List of Book Titles--------------")
                    for each in range(10, len(BookOperation.book_title_list)):
                        print(f"{display_num} {BookOperation.book_title_list[each]}")
                        display_num += 1
                        if display_num > 20:
                            break
                    print("Current Page : 2")
                    print("Total Pages : 10")
                    print("--------------------The End----------------------")
                if page_num == 3:
                    display_num = 21
                    print("----------------List of Book Titles--------------")
                    for each in range(20, len(BookOperation.book_title_list)):
                        print(f"{display_num} {BookOperation.book_title_list[each]}")
                        display_num += 1
                        if display_num > 30:
                            break
                    print("Current Page : 3")
                    print("Total Pages : 10")
                    print("--------------------The End----------------------")
                if page_num == 4:
                    display_num = 31
                    print("----------------List of Book Titles--------------")
                    for each in range(30, len(BookOperation.book_title_list)):
                        print(f"{display_num} {BookOperation.book_title_list[each]}")
                        display_num += 1
                        if display_num > 40:
                            break
                    print("Current Page : 4")
                    print("Total Pages : 10")
                    print("--------------------The End----------------------")
                if page_num == 5:
                    display_num = 41
                    print("----------------List of Book Titles--------------")
                    for each in range(40, len(BookOperation.book_title_list)):
                        print(f"{display_num} {BookOperation.book_title_list[each]}")
                        display_num += 1
                        if display_num > 50:
                            break
                    print("Current Page : 5")
                    print("Total Pages : 10")
                    print("--------------------The End----------------------")
                    #print the book titles depending on the user input of the page number
                if page_num == 6:
                    display_num = 51
                    print("----------------List of Book Titles--------------")
                    for each in range(50, len(BookOperation.book_title_list)):
                        print(f"{display_num} {BookOperation.book_title_list[each]}")
                        display_num += 1
                        if display_num > 60:
                            break
                    print("Current Page : 6")
                    print("Total Pages : 10")
                    print("--------------------The End----------------------")
                if page_num == 7:
                    display_num = 61
                    print("----------------List of Book Titles--------------")
                    for each in range(60, len(BookOperation.book_title_list)):
                        print(f"{display_num} {BookOperation.book_title_list[each]}")
                        display_num += 1
                        if display_num > 70:
                            break
                    print("Current Page : 7")
                    print("Total Pages : 10")
                    print("--------------------The End----------------------")
                if page_num == 8:
                    display_num = 71
                    print("----------------List of Book Titles--------------")
                    for each in range(70, len(BookOperation.book_title_list)):
                        print(f"{display_num} {BookOperation.book_title_list[each]}")
                        display_num += 1
                        if display_num > 80:
                            break
                    print("Current Page : 8")
                    print("Total Pages : 10")
                    print("--------------------The End----------------------")
                if page_num == 9:
                    display_num = 81
                    print("----------------List of Book Titles--------------")
                    for each in range(80, len(BookOperation.book_title_list)):
                        print(f"{display_num} {BookOperation.book_title_list[each]}")
                        display_num += 1
                        if display_num > 90:
                            break
                    print("Current Page : 9")
                    print("Total Pages : 10")
                    print("--------------------The End----------------------")
                if page_num == 10:
                    display_num = 91
                    print("----------------List of Book Titles--------------")
                    for each in range(90, len(BookOperation.book_title_list)):
                        print(f"{display_num} {BookOperation.book_title_list[each]}")
                        display_num += 1
                        if display_num > 99:
                            break
                    print("Current Page : 10")
                    print("Total Pages : 10")

                    print("--------------------The End----------------------")
                    #handling exceptions accordingly
        except ValueError:
            print("please give a valid integer")
        else:
            if page_num > len(BookOperation.book_title_list):
                print("Number is bigger than the number of titles")

    def get_book_by_author(self, author_name):
        """
        gets the author by book title
        attributers
        ---------
        tile_author :
        stores the author titles
        author_list: list
        stores author names
        book_title: list
        stores book titles
        book_num:int
        stores book numbers


        """
        if len(author_name)>0:
            try:
                #opening the books
                with open(BookOperation.book_info_path, 'r', encoding="utf8") as file:
                    tile_author = {}
                    author_list = []
                    book_title = []
                    book_num = 1
                    #getting titles for author names
                    for each_line in file:
                        new_line = each_line.split(";;;")
                        author_list.append(new_line[1])
                        tile_author[new_line[0]] = new_line[1]
                    result_list = [each for each in author_list if author_name.lower() in each.lower()]
                    for name in set(result_list):
                        for key, value in tile_author.items():
                            if value == name:
                                book_title.append(key)
                                #printing the author names according to the input
                    if len(book_title) > 0:
                        print(f"-----------Books by {author_name}------------")
                    else:
                        print("Book not found")
                    for each in book_title:
                        print(f"{book_num}.Book Title {book_num} _ {each}")
                        book_num += 1
                    print("------------------end-------------------")
                    #handling exceptions
            except Exception as e:
                print("Error has occurred:", e)
        else:
            print("Author not found")




    def get_book_release_year(self):
        """
        gets the books released depending on the year
        Attributes
        ---------
        exact_year: list
        stores all the books depending on the year

        """

        try:
            #opening the files to sort depending on the year

            with open(BookOperation.book_info_path, 'r', encoding="utf8") as file:
                exact_year = []
                for each_line in file:
                    new_line = each_line.split(";;;")
                    year_line = new_line[2].split(',')
                    if len(year_line) == 2:
                        exact_year.append(year_line[1])
                before_1990 = 0
                between_years = 0
                after_2000 = 0
                for each in exact_year:
                    year = int(float(each))
                    if year < 1990:
                        before_1990 += 1
                    elif 1990 <= year <= 2000:
                        between_years += 1
                    elif year > 2000:
                        after_2000 += 1
                        #display titles ina format
            print("-----------Total Number of Books------------")
            print("Number of books released before 1990 : ", before_1990)
            print("Number of books released between 1990 and 2000 : ", between_years)
            print("Number of books released after 2000 : ", after_2000)
        except Exception as e:
            print("Error has occurred:", e)


    def show_book_content(self, book_title):
        """
        shows the content page of every book
        bookpath_content: dict
        store the bookpath of the book title
        count_list: list
        stores the list of content index numbers

        """

        try:
            if book_title in BookOperation.book_title_list:
                # openoing all the files and storing the indexes of contents

                bookpath_content = {}
                title_path = ""
                for file in os.listdir(BookOperation.book_folder_path):
                    if file.endswith(".txt"):
                        book_path = f"{BookOperation.book_folder_path}/{file}"
                        with open(book_path, 'r', encoding='utf-8') as f:
                            newlines = 0
                            cont_list = []
                            for l_no, line in enumerate(f):
                                new_line = line.strip()
                                if new_line.startswith('contents') or new_line.startswith('CONTENTS') or new_line.startswith(
                                        'Contents') or new_line.startswith('CONTENTS.') or new_line.startswith(
                                    'CONTENTS:') or new_line.startswith(
                                    'Contents.'):
                                    content_line = new_line
                                    content_no = l_no
                                    break
                                else:
                                    content_no = 0
                            if file not in '24518-0.txt':
                                if 0 < content_no < 250:
                                    for l_no, line in enumerate(f):
                                        if line == '\n':
                                            newlines += 1
                                            if newlines >= 3 and (
                                                    file in ['pg46.txt', 'pg1184.txt', 'pg203.txt', 'pg46.txt', '766-0.txt',
                                                             '205-0.txt', '3600-0.txt', '215-0.txt']):
                                                break
                                            elif newlines >= 2 and (file in ['829-0.txt', '43-0.txt']):
                                                break
                                            elif newlines > 3:
                                                break
                                        else:
                                            newlines = 0
                                        if line not in cont_list:
                                            cont_list.append(line)
                                else:
                                    cont_list.append("NO CONTENT")
                        if file in ['829-0.txt', '43-0.txt','24518-0.txt']:
                            cont_list.append("NO CONTENT")
                        file_content = '\n'.join(str(x.strip()) for x in cont_list)
                        bookpath_content[book_path] = file_content
                        #excluding some of the books which are not in the format required
                #reteiving the content based on the dict and printing them

                with open(BookOperation.book_info_path, 'r', encoding="utf8") as file:
                    for each_line in file:
                        new_line = each_line.split(";;;")
                        if book_title == new_line[0]:
                            title_path = new_line[6]
                for key, value in bookpath_content.items():
                    if os.path.normpath(key) in os.path.normpath(title_path):
                        print(value.strip())
                        #handling the exceptions

        except Exception as e:
            print("Error has occurred:", e)
        except :
            print("Book not Found")
        else:
            print("Book doesn't exits")
    def display_data(self, book_title, page_num):
        """
        displays data based on the book title and page number
        it shows 15 lines of data

        """
        if page_num:

            try:
                #checking if the title exists in the list
                if book_title in BookOperation.book_title_list:
                    book_object = BookOperation.book_info_dict[book_title]
                    book_path = book_object.book_path
                    with open(book_path.strip(), 'r', encoding="utf8") as file:
                        new_data = file.readlines()
                        start_index = (page_num - 1) * 15
                        end_index = page_num * 15

                        if end_index > len(new_data):
                            end_index = len(new_data)
                        for line in range(start_index, end_index):
                            print(new_data[line].strip())
                else:
                    print("Book not Found")

            except Exception as e:
                print("error", e)
        else:
            print("Page number is invalid")

