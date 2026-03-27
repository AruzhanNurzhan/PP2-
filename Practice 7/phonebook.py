import csv
import sys
from connect import init_db, get_conn

def add_contact_console():
    first = input("First name: ").strip()
    phone = input("Phone: ").strip()
    if not first or not phone:
        return
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s) ON CONFLICT (phone) DO NOTHING;", (first, phone))
    conn.commit()
    cur.close()
    conn.close()

def import_csv():
    file = "contacts.csv"
    conn = get_conn()
    cur = conn.cursor()
    with open(file, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            first_name = row[0]
            phone = row[1]
            cur.execute(
                "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s) ON CONFLICT (phone) DO NOTHING;",
                (first_name, phone)
            )
    conn.commit()
    cur.close()
    conn.close()

def search_name():
    name = input("Name to search: ").strip()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, first_name, last_name, phone FROM phonebook WHERE first_name ILIKE %s;", (f"%{name}%",))
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    conn.close()

def delete_contact():
    phone = input("Phone to delete: ").strip()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE phone=%s RETURNING id, first_name;", (phone,))
    conn.commit()
    cur.close()
    conn.close()

def main():
    if input("Create table if not exists? (y/n): ").lower() == "y":
        init_db()
    while True:
        print("\n1.Import CSV  2.Add  3.Search  4.Delete  0.Exit")
        choice = input("Choice: ")
        if choice == "1": import_csv()
        elif choice == "2": add_contact_console()
        elif choice == "3": search_name()
        elif choice == "4": delete_contact()
        elif choice == "0": sys.exit()

if __name__ == "__main__":
    main()