from connect import get_conn

def search(pattern):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_contacts(%s);", (pattern,))
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def upsert(first_name, last_name, phone):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("CALL upsert_contact(%s, %s, %s);",
                (first_name, last_name, phone))
    conn.commit()
    cur.close()
    conn.close()

def bulk_insert(first_names, last_names, phones):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("CALL bulk_insert(%s, %s, %s);",
                (first_names, last_names, phones))
    conn.commit()
    cur.close()
    conn.close()

def paginate(limit, offset):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s);",
                (limit, offset))
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def delete(value):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("CALL delete_contact(%s);", (value,))
    conn.commit()
    cur.close()
    conn.close()

def main():
    while True:
        print("\n1.Search  2.Add/Update  3.Bulk Insert  4.Pagination  5.Delete  0.Exit")
        choice = input("Choice: ")

        if choice == '1':
            pattern = input()
            for r in search(pattern):
                print(r)

        elif choice == '2':
            first_name = input()
            last_name = input()
            phone = input()
            upsert(first_name, last_name, phone)

        elif choice == '3':
            first_names = input().split(",")
            last_names = input().split(",")
            phones = input().split(",")
            if len(first_names) == len(last_names) == len(phones):
                bulk_insert(first_names, last_names, phones)

        elif choice == '4':
            limit = int(input())
            offset = int(input())
            for r in paginate(limit, offset):
                print(r)

        elif choice == '5':
            value = input()
            delete(value)

        elif choice == '0':
            break

if __name__ == "__main__":
    main()