import json
import csv
import os
from connect import get_conn, init_db

# 1. Filter by group
def filter_group():
    g = input("Enter group name: ").strip()
    conn = get_conn()
    cur = conn.cursor()
    # Добавляем %, чтобы поиск был гибким
    cur.execute("""
        SELECT c.first_name, g.name
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        WHERE g.name ILIKE %s
    """, (f"%{g}%",)) 
    
    results = cur.fetchall()
    if not results:
        print(f"No contacts found in group '{g}'. (Try searching for just a few letters)")
    else:
        for r in results:
            print(f"Name: {r[0]} | Group: {r[1]}")
    conn.close()

# 2. Search by email
def search_email():
    e = input("Enter email part: ")
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT first_name, email FROM contacts WHERE email ILIKE %s", (f"%{e}%",))
    results = cur.fetchall()
    for r in results:
        print(f"Name: {r[0]} | Email: {r[1]}")
    conn.close()

# 3. Sort
def sort_contacts():
    print("Sort by: 1) Name 2) Birthday 3) Date added")
    c = input("Choice: ")
    order = "first_name" if c == "1" else "birthday" if c == "2" else "created_at"
    
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(f"SELECT first_name, birthday FROM contacts ORDER BY {order}")
    results = cur.fetchall()
    for r in results:
        print(f"Name: {r[0]} | Info: {r[1]}")
    conn.close()

# 4. Pagination
def paginate():
    limit = 3
    offset = 0
    conn = get_conn()
    cur = conn.cursor()
    while True:
        cur.execute("SELECT first_name, last_name FROM contacts LIMIT %s OFFSET %s", (limit, offset))
        rows = cur.fetchall()
        if not rows and offset > 0:
            print("No more contacts.")
            offset -= limit
            continue
        for r in rows:
            print(f"- {r[0]} {r[1]}")
        
        cmd = input("\n[n]ext / [p]rev / [q]uit: ").lower()
        if cmd == "n": offset += limit
        elif cmd == "p": offset = max(0, offset - limit)
        else: break
    conn.close()

# 5. Export JSON
def export_json():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT c.first_name, c.last_name, c.email, c.birthday, g.name as group_name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
    """)
    rows = cur.fetchall()
    # Конвертируем даты в строки для JSON
    data = []
    for r in rows:
        data.append({
            "first_name": r[0], "last_name": r[1], 
            "email": r[2], "birthday": str(r[3]) if r[3] else None, 
            "group": r[4]
        })
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print("Exported to data.json")
    conn.close()

# 6. Import CSV (Extended)
def import_csv():
    conn = get_conn()
    cur = conn.cursor()
    try:
        with open("contacts.csv", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            
            # Убираем лишние пробелы из имен колонок, если они есть
            reader.fieldnames = [name.strip() for name in reader.fieldnames]
            
            for row in reader:
                # Пропускаем пустые строки
                if not row.get('first_name'):
                    continue

                # 1. Группа
                g_name = (row.get('group') or 'Other').strip()
                cur.execute("INSERT INTO groups(name) VALUES(%s) ON CONFLICT DO NOTHING", (g_name,))
                cur.execute("SELECT id FROM groups WHERE name=%s", (g_name,))
                gid = cur.fetchone()[0]

                # 2. Контакт
                cur.execute("""
                    INSERT INTO contacts(first_name, last_name, email, birthday, group_id)
                    VALUES(%s, %s, %s, %s, %s) RETURNING id
                """, (
                    row['first_name'].strip(), 
                    row.get('last_name', '').strip(), 
                    row.get('email', '').strip(), 
                    row.get('birthday') or None, 
                    gid
                ))
                cid = cur.fetchone()[0]

                # 3. Телефон
                cur.execute("INSERT INTO phones(contact_id, phone, type) VALUES(%s, %s, %s)", 
                            (cid, row['phone'].strip(), row.get('phone_type', 'mobile').strip()))
        
        conn.commit()
        print("✅ Success! CSV Imported.")
    except KeyError as e:
        print(f"❌ Error: Python can't find column {e}. Check your CSV header!")
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.rollback()
    finally:
        conn.close()

# 7. Add phone (Procedure)
def add_phone():
    name = input("Contact Name: ")
    phone = input("New Phone: ")
    ptype = input("Type (home/work/mobile): ")
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, ptype))
        conn.commit()
        print("Phone added!")
    except Exception as e:
        print(f"Error: {e}")
    conn.close()

# 8. Move group (Procedure)
def move_group():
    name = input("Contact Name: ")
    group = input("New Group Name: ")
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("CALL move_to_group(%s, %s)", (name, group))
    conn.commit()
    print("Group updated!")
    conn.close()

# 9. Search all (Function)
def search_all():
    q = input("Global search: ").strip()
    if not q:
        return

    conn = get_conn()
    cur = conn.cursor()
    try:
        # SELECT * заберет все колонки, которые выдает search_contacts
        cur.execute("SELECT * FROM search_contacts(%s)", (q,))
        results = cur.fetchall()
        
        if not results:
            print(f"No contacts matched '{q}'.")
        else:
            print(f"\n--- Found {len(results)} matches ---")
            for r in results:
                # Берем данные по индексам: 0-id, 1-first_name, 2-last_name, 3-email
                print(f"ID: {r[0]} | Name: {r[1]} {r[2]} | Email: {r[3] or 'N/A'}")
    except Exception as e:
        print(f"Search error: {e}")
    finally:
        conn.close()

def main():
    if input("Init DB? (y/n): ").lower() == "y":
        init_db()

    while True:
        print("\n--- MENU ---")
        print("1:Filter 2:Email 3:Sort 4:Page 5:Export 6:ImportCSV 7:AddPhone 8:Move 9:Search 0:Exit")
        c = input("Select: ")

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