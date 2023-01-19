import models

def show_books():
    books = models.Book.select()
    if books is not None:
        return "Not found..."
    else:
        return books


def register(username, password):
    user = models.User()
    user.username = username
    user.password = password
    user.save()
    return 'You register sucsessfully..'


def login(usernames, passwords):
    users = models.User.select()
    for user in users:
        if user.username == usernames and user.password == passwords:
            return user.username
        return "Guest"

