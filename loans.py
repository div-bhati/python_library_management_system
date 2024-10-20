from database_connection import create_connection
from datetime import date

def borrow_book(conn,book_id, member_id):
    cursor=conn.cursor()
    today = date.today()
    due_date = today.replace(day=today.day+14)

    cursor.execute("SELECT copies_available from books where book_id = %s", (book_id,))
    result = cursor.fetchone()

    if result and result[0]>0:
        query = """INSERT INTO loans (book_id, member_id, loan_date, due_date)
        values(%s, %s, %s, %s)"""
        cursor.execute(query,(book_id,member_id,today,due_date))
        cursor.execute("UPDATE books  set copies_availbale = -1 where book_id = %s",( book_id,))
        conn.commit()
        print("Book borrowed successfully!!")
    else:
        print("Sorry book is not available.")

def return_book(conn,loan_id):
    cursor = conn.cursor()
    cursor.execute("Select book_id from loans where loan_id =%s", (loan_id,))
    book_id = cursor.fetchone()

    if book_id:
        cursor.execute("UPDATE Loans set return_date=%s where loan_id = %s",(date.today(),loan_id))
        cursor.execute("UPDATE books set copies_available = copies_available+1 where book_id=%s",(book_id[0],))
        cursor.commit()
        print("Book returned successfully!")
    else:
        print("Loan ID not found.")