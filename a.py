class Book:
    def __init__(self, title, author):
      self.title = title
      self.author = author
      self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed == False:
           self.is_borrowed == True
           print(self.title, "has been borrowed")
        else:
           print(self.title,"is alredy borrowed")

    def return_book(self):
       if self.is_borrowed == True:
          self.is_borrowed = False
          print(self.title, "has been returned")
       else:
          print(self.title, "was not borrowed")

book1 = Book("harry potter" , "J.K Rowling")
book2 = Book("DNA", "James Watson")
book3 = Book("Lion,Witch, And The Wodrobe", "C.S Lewis")

book1.borrow()
book1.return_book()

book2.borrow()
book2.return_book

book3.borrow()
book3.return_book

