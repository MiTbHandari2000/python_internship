print("\n--- Create Book class to store its details and show details ---")


class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"Book Title:{self.title} Book Author: {self.author} Book Price: {self.price}"
        
book1 = Book("Atomic-Habbits","James Clear","$50")
print(book1)
