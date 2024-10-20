from database_connection import create_connection
from books import add_book, view_books, update_book, delete_book
from members import add_member, view_members, delete_member
from loans import borrow_book, return_book

def main():
    conn = create_connection()
    if not conn:
        return

    while True:
        print("\nLibrary Management System")
        print("1. Manage Books")
        print("2. Manage Members")
        print("3. Manage Loans")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                print("\nBook Management")
                print("1. Add Book")
                print("2. View Books")
                print("3. Update Book")
                print("4. Delete Book")
                print("5. Back")
                book_choice = input("Enter your choice: ")

                if book_choice == '1':
                    title = input("Enter book title: ")
                    author = input("Enter book author: ")
                    publisher = input("Enter book publisher: ")
                    published_year = input("Enter published year: ")
                    isbn = input("Enter ISBN: ")
                    total_copies = int(input("Enter total copies: "))
                    add_book(conn, title, author, publisher, published_year, isbn, total_copies)

                elif book_choice == '2':
                    view_books(conn)

                elif book_choice == '3':
                    book_id = int(input("Enter book ID to update: "))
                    title = input("Enter new book title: ")
                    author = input("Enter new book author: ")
                    publisher = input("Enter new book publisher: ")
                    published_year = input("Enter new published year: ")
                    isbn = input("Enter new ISBN: ")
                    total_copies = int(input("Enter new total copies: "))
                    update_book(conn, book_id, title, author, publisher, published_year, isbn, total_copies)

                elif book_choice == '4':
                    book_id = int(input("Enter book ID to delete: "))
                    delete_book(conn, book_id)

                elif book_choice == '5':
                    break

                else:
                    print("Invalid choice. Please try again.")

        elif choice == '2':
            while True:
                print("\nMember Management")
                print("1. Add Member")
                print("2. View Members")
                print("3. Delete Member")
                print("4. Back")
                member_choice = input("Enter your choice: ")

                if member_choice == '1':
                    name = input("Enter member name: ")
                    email = input("Enter member email: ")
                    phone = input("Enter member phone: ")
                    join_date = input("Enter join date (YYYY-MM-DD): ")
                    membership_type = input("Enter membership type: ")
                    add_member(conn, name, email, phone, join_date, membership_type)

                elif member_choice == '2':
                    view_members(conn)

                elif member_choice == '3':
                    member_id = int(input("Enter member ID to delete: "))
                    delete_member(conn, member_id)

                elif member_choice == '4':
                    break

                else:
                    print("Invalid choice. Please try again.")

        elif choice == '3':
            while True:
                print("\nLoan Management")
                print("1. Borrow Book")
                print("2. Return Book")
                print("3. Back")
                loan_choice = input("Enter your choice: ")

                if loan_choice == '1':
                    book_id = int(input("Enter book ID to borrow: "))
                    member_id = int(input("Enter member ID: "))
                    borrow_book(conn, book_id, member_id)

                elif loan_choice == '2':
                    loan_id = int(input("Enter loan ID to return: "))
                    return_book(conn, loan_id)

                elif loan_choice == '3':
                    break

                else:
                    print("Invalid choice. Please try again.")

        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

    if conn.is_connected():
        conn.close()

if __name__ == '__main__':
    main()
