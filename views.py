import models

def show_books():
    books = models.Book.select()
    if books is None:
        return "Not found..."
    return books


def register(username, password):
    user = models.User()
    user.username = username
    user.password = password
    user.save()
    create_default_shelves(user.id)
    return 'You register sucsessfully..'


def login(usernames, passwords):
    users = models.User.select()
    for user in users:
        if user.username == usernames and user.password == passwords:
            return user.username
        return "Guest"


def add_book(isbn, name):
    book = models.Book.create(isbn=isbn, name=name)
    return f"Book: {book.name}, ISBN: {book.isbn}"


def show_shelves(username):
    user = models.User.select().where(models.User.username == username).get()
    # shelves = models.Shelf.select().where(models.Shelf.user == user.id)
    
    return user.shelves


def create_default_shelves(id):
    for shelf in models.Shelf.DEFAULT_SHELVES:
        models.Shelf.create(name=shelf, user = id)
 
    

def new_shelf(username, shelf_name):
    user = models.User.get(models.User.username == username)
    new_shelf = models.Shelf.create(name=shelf_name, user=user.id)
    
    return user.shelves