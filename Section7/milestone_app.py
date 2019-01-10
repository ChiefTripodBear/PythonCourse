from utils import database

user_choice = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your Choice: """

def menu():
    user_input = input(user_choice)
    while user_input != 'q':
        pass
    
#def prompt_add_book() - ask for book name and author
#def list_books() - show all the books in our list
#def prompt_read_book() - ask for book name and change it to 'read' in our list
#def prompt_delete_book() - ask for book name and remove book from list

