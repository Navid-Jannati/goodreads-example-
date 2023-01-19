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
            '10. Exit...'
            )
        print()
        status = int(input('What do you want? (insert number): '))
        # Regist
        if status == 1:
            username = input('Enter "Username": ')
            password = input('Enter "Password": ')
            print(views.register(username, password))
            
        
        elif status == 2:
            username = input('Enter "Username": ')
            password = input('Enter "Password": ')
            user_client =  views.login(username, password)

        




        elif status == 10:
            exit()
            



        print('*' * 80)