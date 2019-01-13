import sqlite3

"""
Concerned with storing and retrieving books from a list.
Format of the csv file:

[
        {
                'name': 'Clean Code',
                'author': 'Robert',
                'read': True
        }
]
"""

def create_book_table():
    connection = sqlite3.connect('Section7/data/data.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')
    connection.commit()
    connection.close()

# adds a book to our dictionary
def add_book(name, author):
    connection = sqlite3.connect('Section7/data/data.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))

    connection.commit()
    connection.close()


# returns the dictionary of all books
def get_all_books():
    connection = sqlite3.connect('Section7/data/data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * from books')
    #a list of tuples [(name, author, read), (name, author, read)]
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    connection.close()

    return books


# marks a book as read, given the book name from the user
def mark_book_as_read(name):
    connection = sqlite3.connect('Section7/data/data.db')
    cursor = connection.cursor()

    cursor.execute('UPDATE books SET read = 1 WHERE name = ?', (name,))
    connection.commit()
    connection.close()


# deletes a book from the dictionary
def delete_book(name):
    connection = sqlite3.connect('Section7/data/data.db')
    cursor = connection.cursor()

    cursor.execute('DELETE from books WHERE name = ?', (name,))
    connection.commit()
    connection.close()
