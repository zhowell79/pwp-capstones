class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print('Email address updated to:' + self.email)

    def __repr__(self):
        print ('User {}, email: {}, books read: {}'.format(self.name, self.email, len(self.books)))

    def __eq__(self, other_user):
        if self.email == other_user.email and self.name == other_user.email:
            return True
        else:
            return False

class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print('ISBN address updated to:' + self.isbn)

    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else: 
            return False

    def __repr__(self):
        print('Book Info: Title: {}, ISBN: {}'.format(self.title, str(self.isbn))

new_book = Book('Alice In Wonderland', 12345)
#print(new_book)
#novel1.set
# _isbn(9781536831139)
#nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
#nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
#novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
#novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
#user1 = User("Alan Turing", "alan@turing.com")
#user2 = User("David Marr", "david@computation.org")