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
        return ('User {}, email: {}, books read: {}'.format(self.name, self.email, str(len(self.books))))

    def __eq__(self, other_user):
        if self.email == other_user.email and self.name == other_user.email:
            return True
        else:
            return False

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        rating_sum = 0
        for rating in self.books.values():
            rating_sum += rating

        # return average rating
        return rating_sum / len(self.books)

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
        print('ISBN address updated to:' + str(self.isbn))

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
        return ('(Book) {}, ISBN: {}'.format(self.title, str(self.isbn)))

    def get_average_rating(self):
        rating_sum = 0
        for rating in self.ratings:
            rating_sum += rating

        # return average rating
        if len(self.ratings) > 0:
            return rating_sum / len(self.ratings)
        else: 
            print("There were no ratings!")

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
        
    def get_author(self):
        return self.author

    def __repr__(self):
        return ('(Fiction) {} by {}, ISBN: {}'.format(self.title, self.author, str(self.isbn)))

class NonFiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
            
    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return ('(Non-Fiction) {}, a {} manual on {}, ISBN: {}'.format(self.title, self.level, self.subject, str(self.isbn)))

class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        self.books[new_book] = 0
        return new_book

    def create_novel(self, title, author, isbn):
        new_book = Fiction(title, author, isbn)
        self.books[new_book] = 0
        return new_book    

    def create_non_fiction(self, title, subject, level, isbn):
        new_book = NonFiction(title, subject, level, isbn)
        self.books[new_book] = 0
        return new_book    

    def add_book_to_user(self, book, email, rating="None"):
        if email in self.users:
            self.users[email].read_book(book, rating)
            book.add_rating(rating)

            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email: " + str(email))

    def add_user(self, name, email, user_books=[]):
        new_user = User(name, email)
        if len(user_books) > 0:
            for book in user_books:
                self.add_book_to_user(book, email)

        self.users[email] = new_user

    def print_catalog(self):
        for books in self.books:
            print(books)

    def print_users(self):
        for val in self.users.values():
            print(val)

    def get_most_read_book(self):
        return max(self.books, key=self.books.get)

    def highest_rated_book(self):
        books_ratings = {}

        for key in self.books:
            if key.get_average_rating() != None:
                books_ratings[key] = key.get_average_rating()

        return max(books_ratings, key=books_ratings.get)

    def most_positive_user(self):
        user_avg_rating = {}
        winner_avg = 0.0
        winner_index = 0 

        for val in self.users.values():
            if val.get_average_rating() != None:
                user_avg_rating[val.get_average_rating()] = val
                if val.get_average_rating() > winner_avg:
                    winner_avg = val.get_average_rating()
                    winner_index = val

        return winner_index
