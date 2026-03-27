import psycopg2
from config import DB_CONFIG

def get_conn():
    return psycopg2.connect(**DB_CONFIG)

def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name  NOT NULL,
            last_name TEXT,
            phone x UNIQUE NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()