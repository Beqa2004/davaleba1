class LibraryAccount:
    def __init__(self, username, level="Basic"):
        self.username = username
        self.level = level
        self.borrowed_books = 0
        self.limit = self.borrow_limit()

    def borrow_limit(self):
        if self.level == "Basic":
            return 3
        if self.level == "Premium":
            return 6
        if self.level == "Elite":
            return 9
        else:
            return 1
        
    def check_out(self, book_number):
        if book_number > 0 and (book_number + self.borrowed_books) <= self.borrow_limit():
            self.borrowed_books += book_number
            print(f"Total books borrowed: {self.borrowed_books}")
        elif (book_number + self.borrowed_books) > self.borrow_limit():
            print(f"You've reached your limit of {self.borrow_limit()} books")

        else:
            print("Something went wrong")

    def return_books(self, book_number):
        if book_number > 0 and book_number <= self.borrowed_books:
            self.borrowed_books -= book_number
            print(f"Your current amount of books that you have borrowed is {self.borrowed_books}")
        else:
            print("Something went wrong")


class BasicAccount(LibraryAccount):
    def __init__(self, username):
        super().__init__(username, level="Basic") 

    
class PremiumAccount(LibraryAccount):
    def __init__(self, username):
        super().__init__(username, level="Premium")

    def borrow_limit(self):
        return 6
        
class EliteAccount(LibraryAccount):
    def __init__(self, username):
        super().__init__(username, level="Elite")   

    def borrow_limit(self):
        return 9

    
basic = BasicAccount("beqa")
basic.check_out(3)
basic.return_books(1)