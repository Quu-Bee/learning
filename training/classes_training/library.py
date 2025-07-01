from book_template import template

# class Book:
#     def __init__(self, title):
#         self.title = title

#     def change_title(self, new_title):
#         self.title = new_title

#     def get_title(self):
#         return f"title: {self.title}"

# book1 = Book("bim bim")

# book1.change_title("bom bom")
# print(book1.get_title())


class Book:
    def __init__(self, title, author, pages):
        self.__title = title
        self.author = author
        self.pages = pages

    @property
    def title(self):
        return f"title: {self.title}"

    @title.setter
    def title(self, new_title: str):
        if isinstance(new_title, str):
            self.title = new_title
        else:
            raise Exception("! Error !")

    def get_info(self):
        return template.format(
            title=self.__title,
            author=self.author,
            pages=self.pages,
        )


class Library:
    def __init__(self):
        self.book_list: list[Book] = []

    def add_book(self, book):
        if book not in self.book_list:
            self.book_list.append(book)

    def show_books(self):
        al_book_list = []
        for book in self.book_list:
            al_book_list.append(book.get_info())
        return al_book_list


book1 = Book("bim bim", "bam bam", 228)
book2 = Book("Bum bum", "boom boom", 52)
library1 = Library()
library1.add_book(book1)
library1.add_book(book2)
print(*library1.show_books(), sep="\n\n")
