# python program to implement class for academic course and book

# class for Academic course
class Course:
    
    def __init__(self, course_name, course_duration, *books):
        self.course_name = course_name
        self.course_duration = course_duration
        self.books = [self.Book(book_title) for book_title in books]
    
    def show_details(self):
        print('-'*3+' Course Details '+'-'*3)
        print('Name :', self.course_name)
        print('Duration :', self.course_duration)
        print('-'+' Suggested Books List '+'-')
        
        for book in self.books:
            print(book)
        
    
    class Book:
        def __init__(self, title):
            self.title = title
        
        def __str__(self):
            return self.title
        
# creating object for Course class
c1 = Course('Bigdata Analytics', '75 hrs', 'Big data tenure', 'Bigger sized data analytics', 'Large size data analytics')

c1.show_details()