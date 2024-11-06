# python program to implement a class for book details

# class for book
class Book:
    
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def show_details(self):
        print(f'--- Book Details ---   \nTitle : {self.title} \nAuthor : {self.author} \nPrice : {self.price}')
    
# creating object for book class
b = Book('Calculus', 'Jeremy', 1000)

b.show_details()