import sys
from PyQt5 import QtWidgets
from main_window1 import Ui_MainWindow
from miyan_tearm_back1 import Ketab, Manage

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_add.clicked.connect(self.add_book)
        self.pushButton_delete.clicked.connect(self.delete_book)
        self.pushButton_search.clicked.connect(self.search_book)
        self.pushButton_list.clicked.connect(self.list_books)

    def add_book(self):
        name = self.lineEdit_name.text()
        author = self.lineEdit_author.text()
        publish_year = self.lineEdit_year.text()
        book_type = self.lineEdit_type.text()
        if name and author and publish_year and book_type:
            book = Ketab(name, author, publish_year, book_type)
            Manage.add(book)
            self.textEdit_results.append("Book added successfully.")
        else:
            self.textEdit_results.append("Please fill all fields.")
        self.clear_inputs()

    def delete_book(self):
        key = self.lineEdit_name.text() or self.lineEdit_author.text() or self.lineEdit_year.text() or self.lineEdit_type.text()
        if key:
            result = Manage.delete(key)
            if result:
                self.textEdit_results.append("Book deleted successfully.")
            else:
                self.textEdit_results.append("Book not found.")
        else:
            self.textEdit_results.append("Please provide a key for deletion.")
        self.clear_inputs()

    def search_book(self):
        key = self.lineEdit_name.text() or self.lineEdit_author.text() or self.lineEdit_year.text() or self.lineEdit_type.text()
        if key:
            self.textEdit_results.clear()
            found_books = Manage.search(key)
            if found_books:
                for book in found_books:
                    self.textEdit_results.append(book)
                    self.textEdit_results.append("\n")
            else:
                self.textEdit_results.append("Book not found.")
        else:
            self.textEdit_results.append("Please provide a key for searching.")
        self.clear_inputs()

    def list_books(self):
        self.textEdit_results.clear()
        all_books = Manage.list_all_books()
        if all_books:
            for book in all_books:
                self.textEdit_results.append(book)
                self.textEdit_results.append("\n")
        else:
            self.textEdit_results.append("No books found.")
        self.clear_inputs()

    def clear_inputs(self):
        self.lineEdit_name.clear()
        self.lineEdit_author.clear()
        self.lineEdit_year.clear()
        self.lineEdit_type.clear()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
