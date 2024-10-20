from database_connection import create_connection

def add_member(conn, name, email, phone, join_date, membership_type):
    cursor=conn.cursor()
    query = """INSERT INTO members (name, email, phone, join_date, membership_type)
    values(%s, %s, %s, %s, %s)"""
    cursor.execute(query, (name,email,phone, join_date, membership_type))
    conn.commit()
    print("Member dded successfully!")

def view_members(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * from members")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No members found!")

def delete_member(conn, member_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM members where member_id = %s",(member_id,))
    conn.commit()
    print("Member deleted successfully!!")

