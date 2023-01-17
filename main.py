from models import database, Author, Book, BookAuthor, BookShelf, BookTranslator, User, Shelf, UserAuthorRelation, UserRelation





def create_table():
    database.create_tables([Author, Book, BookAuthor, BookShelf, BookTranslator, User, Shelf, UserAuthorRelation, UserRelation])





if __name__ == "__main__":
    # print('Hi Goodreads')
    # create_table()
    pass