Books = []  # List untuk menyimpan buku


class Book:
    def __init__(self, title, author, isbn, is_borrowed=False):  # membuat atribute
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = is_borrowed

    def __repr__(self):
        return (f"Book title \t= {self.title}\n "
                f"Author \t= {self.author}\n "
                f"Isbn Number \t= {self.isbn}\n"
                f'Loan status \t= {'Yes' if self.is_borrowed else 'No'}')

    def borrow(self, name):  # method untuk peminjaman buku
        if not self.is_borrowed:
            print(f'Book with title{self.title} is borrowed by {name}')
            self.is_borrowed = True
        else:
            print(f'Book with title "{self.title}" already borrowed')

    def return_book(self, name):  # method untuk pengembalian buku
        if self.is_borrowed:
            print(f'{name} returning book with title "{self.title}".')
            self.is_borrowed = False
        else:
            print(f'Book with title "{self.title}" is not being borrowed')

    def display_info(self,):  # method untuk menampilkan informasi buku
        print(f"Title \t= {self.title}")
        print(f"Writer \t= {self.author}")
        print(f"Isbn Number \t= {self.isbn}")
        print(f"This book {'is borrowed' if self.is_borrowed else ' is ready in library'}")


class Library:
    def __init__(self, ):
        self.books = []

    def add_books(self, book):  # method untuk menambahkan buku
        # memeriksa apakah objek yang akan ditambahkan adalah instance dari class Book
        if isinstance(book, Book):
            self.books.append(book)
            print(f'Book with title "{book.title}" has added to library')

    def display_books(self):  # method untuk menampilkan semua buku
        if self.books:
            print('Books available in library:')
            for book in self.books:
                print(book)
        else:
            print('No available books in library')


# * contoh penggunaan

# membuat objek buku
library = Library()
book_1 = Book('Essential Grammar In Use', 'Raymond Murphy', 9781108586627)
book_2 = Book('English Grammar In Use', 'Raymond Murphy', 9781108457651)

# memasukkan objek buku ke library
library.add_books(book_1)
library.add_books(book_2)

# menampilkan semua buku di library
library.display_books()

# meminjam mengembalikan buku di library
book_2.borrow('en sabah noor')
book_2.return_book('en sabah noor')

# menampilkan informasi tentang buku
book_2.display_info()