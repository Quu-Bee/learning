class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def show_information(self):
        print(f"Название:{self.title}\nАвтор:{self.author}\nГод издания:{self.year}")


class BookList:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            book.show_information()


book_list = BookList()
book_1 = Book("Мастер и Маргарита", "Михаил Афанасьевич Булгаков", 1967)
book_2 = Book("бим бим бам бам", "Саня Журавль", 2025)
book_list.add_book(book_1)
book_list.add_book(book_2)

book_list.show_books()
