from database_connection import create_connection

def add_book(conn, title, author, publisher, published_year, isbn, total_copies):
    cursor= conn.cursor()
    query = """INSERT INTO books(title, author, publisher, published_year, isbn, total_copies, copies_available)
    values (%s, %s, %s, %s, %s, %s, %s)"""

    cursor.execute(query, (title, author, publisher, published_year, isbn, total_copies, total_copies))
    conn.commit()
    print("Book added successfully!!")

def view_books(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books;")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No books found.")

def update_book(conn, book_id, title, author, publisher, published_year, isbn, total_copies):
    cursor = conn.cursor()
    query = """UPDATE BOOKS SET title = %s, author = %s, publisher = %s, published_year = %s, isbn= %s 
    total_copies = %s, copies_available = %s where book_id = %s"""
    cursor.execute(query,(title, author,publisher,published_year,isbn,total_copies,total_copies,book_id))
    conn.commit()
    print("Book updates successfully!")

def delete_book(conn, book_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books where book_id =%s", (book_id))
    conn.commit()
    print("Book deleted successfully!!")

