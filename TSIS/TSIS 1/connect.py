import psycopg2
import os
from config import DB_CONFIG

def get_conn():
    return psycopg2.connect(**DB_CONFIG)

def init_db():
    conn = get_conn()
    cur = conn.cursor()

    base = os.path.dirname(os.path.abspath(__file__))

    for file in ["schema.sql", "procedures.sql"]:
        with open(os.path.join(base, file), encoding="utf-8") as f:
            cur.execute(f.read())

    conn.commit()
    cur.close()
    conn.close()