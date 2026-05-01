import json
import csv
from connect import get_conn, init_db

# filter by group
def filter_group():
    g = input("group: ")

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.first_name, g.name
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        WHERE g.name = %s
    """, (g,))

    print(cur.fetchall())
    conn.close()


# search by email
def search_email():
    e = input("email: ")

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT first_name,email FROM contacts WHERE email ILIKE %s", (f"%{e}%",))
    print(cur.fetchall())

    conn.close()


# sort
def sort_contacts():
    print("1 name 2 birthday 3 date")
    c = input()

    order = "first_name" if c == "1" else "birthday" if c == "2" else "created_at"

    conn = get_conn()
    cur = conn.cursor()

    cur.execute(f"SELECT first_name FROM contacts ORDER BY {order}")
    print(cur.fetchall())

    conn.close()


# pagination (only UI)
def paginate():
    limit = 3
    offset = 0

    conn = get_conn()
    cur = conn.cursor()

    while True:
        cur.execute("SELECT first_name FROM contacts LIMIT %s OFFSET %s", (limit, offset))
        print(cur.fetchall())

        cmd = input("next/prev/quit: ")

        if cmd == "next":
            offset += limit
        elif cmd == "prev":
            offset = max(0, offset - limit)
        else:
            break

    conn.close()


# export json
def export_json():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.first_name, c.email, g.name, p.phone
        FROM contacts c
        LEFT JOIN groups g ON c.group_id=g.id
        LEFT JOIN phones p ON p.contact_id=c.id
    """)

    data = cur.fetchall()

    with open("data.json","w") as f:
        json.dump(data,f)

    conn.close()


# import csv extended
def import_csv():
    conn = get_conn()
    cur = conn.cursor()

    with open("contacts.csv") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            first,last,email,birthday,group,phone,ptype = row

            cur.execute("INSERT INTO groups(name) VALUES(%s) ON CONFLICT DO NOTHING",(group,))
            cur.execute("SELECT id FROM groups WHERE name=%s",(group,))
            gid = cur.fetchone()[0]

            cur.execute("""
                INSERT INTO contacts(first_name,last_name,email,birthday,group_id)
                VALUES(%s,%s,%s,%s,%s) RETURNING id
            """,(first,last,email,birthday,gid))

            cid = cur.fetchone()[0]

            cur.execute("INSERT INTO phones(contact_id,phone,type) VALUES(%s,%s,%s)",(cid,phone,ptype))

    conn.commit()
    conn.close()


# call procedures
def add_phone():
    name = input()
    phone = input()
    t = input()

    conn = get_conn()
    cur = conn.cursor()
    cur.execute("CALL add_phone(%s,%s,%s)",(name,phone,t))
    conn.commit()
    conn.close()


def move_group():
    name = input()
    group = input()

    conn = get_conn()
    cur = conn.cursor()
    cur.execute("CALL move_to_group(%s,%s)",(name,group))
    conn.commit()
    conn.close()


def search_all():
    q = input()

    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_contacts(%s)",(q,))
    print(cur.fetchall())
    conn.close()


def main():
    if input("init db? y/n: ") == "y":
        init_db()

    while True:
        print("1 filter 2 email 3 sort 4 page 5 export 6 import 7 addphone 8 move 9 search 0 exit")
        c = input()

        if c == "1": filter_group()
        elif c == "2": search_email()
        elif c == "3": sort_contacts()
        elif c == "4": paginate()
        elif c == "5": export_json()
        elif c == "6": import_csv()
        elif c == "7": add_phone()
        elif c == "8": move_group()
        elif c == "9": search_all()
        elif c == "0": break


if __name__ == "__main__":
    main()