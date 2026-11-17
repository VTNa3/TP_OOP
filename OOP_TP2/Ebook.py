class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, book_price):
        if book_price >= 0:
            self._price = book_price
        else:
            print("Price cannot be negative.")
            
    print("Physical Book Information:")
    
    def display(self):
            print(f"\tTitle: {self.title}")
            print(f"\tAuthor: {self.author}")
            print(f"\tPrice: ${self._price}")

class EBook(Book):
    def __init__(self, title, author, price, file_size):
        super().__init__(title, author, price)
        self.file_size = file_size

    def display(self):
        print("E-Book Information:")
        super().display()
        print(f"\tFile size: {self.file_size} MB")

atomic_habit = Book("Atomic Habits", "James Clear", 20)
atomic_habit.display()

e_atomic_habit = EBook("Atomic Habits", "James Clear", 5, 3.9)
e_atomic_habit.display()

atomic_habit.set_price(-7)  # This will trigger the error message for negative price