class Ketab:
    def __init__(self, name, author, sal_sakht, book_type):
        self.name = name
        self.author = author
        self.sal_sakht = sal_sakht
        self.book_type = book_type

class Manage:
    @staticmethod
    def add(book):
        with open("book_list.txt", "a") as file:
            file.write(f"{book.name}||{book.author}||{book.sal_sakht}||{book.book_type}\n")

    @staticmethod
    def search(key):
        found_books = []
        s = 1
        with open("book_list.txt", "r") as file:
            for line in file:
                book_info = line.strip().split("||")
                if any(key.lower() in info.lower() for info in book_info):
                    found_books.append(f"{s}. Name: {book_info[0]}, Author: {book_info[1]}, Publish Year: {book_info[2]}, Type: {book_info[3]}")
                    s = s + 1
        return found_books

    @staticmethod
    def list_all_books():
        all_books = []
        s = 1
        with open("book_list.txt", "r") as file:
            for line in file:
                book_info = line.strip().split("||")
                all_books.append(f"{s}. Name: {book_info[0]}, Author: {book_info[1]}, Publish Year: {book_info[2]}, Type: {book_info[3]}")
                s = s+1
        return all_books

    @staticmethod
    def delete(key):
        found = False
        with open("book_list.txt", "r") as file:
            lines = file.readlines()

        with open("book_list.txt", "w") as file:
            for line in lines:
                book_info = line.strip().split("||")
                if any(key.lower() in info.lower() for info in book_info):
                    found = True
                else:
                    file.write(line)

        return found
