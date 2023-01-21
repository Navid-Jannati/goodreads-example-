from models import database, Author, Book, BookAuthor, BookShelf, BookTranslator, User, Shelf, UserAuthorRelation, UserRelation
import views





def create_table():
    database.create_tables([Author, Book, BookAuthor, BookShelf,
    BookTranslator, User, Shelf, UserAuthorRelation, UserRelation])





if __name__ == "__main__":

    program_run_status = True
    user_client = 'guest'


    while program_run_status:
        print('*' * 80)
        if user_client == 'guest':
            print('-------------------------')
            print('User: Guest')
            print('-------------------------')
            print()
        else:
            print('-------------------------')
            print(f'User: {user_client}')
            print('-------------------------')
            print()

# Program start with here.................................................................
        print(
            '1. Register ...\n'
            '2. Login ...\n'
            '3. Show books...\n'
            '4. Add books...\n'
            '5. Show shelves...\n'
            '6. New shelf...\n'
            '10. Exit...'
            )
        print()
        status = int(input('What do you want? (insert number): '))
        print('*' * 80)
        # Regist
        if status == 1:
            username = input('Enter "Username": ')
            password = input('Enter "Password": ')
            print(views.register(username, password))
            
        
        elif status == 2:
            username = input('Enter "Username": ')
            password = input('Enter "Password": ')
            user_client =  views.login(username, password)

        elif status == 3:
            books = views.show_books()
            for book in books:
                print(f"Book: {book.name}.\t, ISBN: {book.isbn}")

        elif status == 4:
            if user_client == 'guest':
                print('Plese Login')
            else:
                book_name = input("Enter name of book: ")
                book_isbn = input("Enter ISBN of book: ")
                print(views.add_book(book_isbn, book_name))
            

        elif status == 5:
            if user_client == 'guest':
                print('Please Login')
            else:
                shelves = views.show_shelves(user_client)
                print(f"Shelves for {user_client}:")
                for shelf in shelves:
                    print(shelf.name)

        elif status == 6:
            if user_client == 'guest':
                print('Please Login')
            else:
                shelf_name = input('Enter name of new shelf: ')
                shelves = views.new_shelf(user_client, shelf_name)
                for shelf in shelves:
                    print(shelf.name)

        




        elif status == 10:
            exit()
            



    print('*' * 80)