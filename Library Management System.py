class Library:
    books=['Programming Fundamentals','Calculus & Analytical Geometrt','Object Oriented Programing',
           'Data Structures',"Discrete Structures"
           ]
    
    no_of_books=len(books)
    def add_book(self):
         new_book=input("Enter the book you want to add in library: ")
         books+=new_book
