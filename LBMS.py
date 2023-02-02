class Library:
      def __init__(self,name):
            self.books = [] # this variable belongs to object not class
            self.name = name
      
      def addbook(self,book_title,author_name,book_category):
            self.books.append({"title":book_title, "author": author_name, "category": book_category})
      
      def giveinfo(self):
            print(f"Our library name is {self.name}")
            print(f"there are {len(self.books)} no of books in our library ")
            for book in self.books:
                  print(book)

lbr1 = Library("Mysore")
lbr1.addbook("harry","karthik","entertainment")
lbr1.addbook("harry","karthik","entertainment")
lbr1.addbook("harry","karthik","entertainment")
lbr1.addbook("harry","karthik","entertainment")
lbr1.addbook("harry","karthik","entertainment")
lbr1.giveinfo()
