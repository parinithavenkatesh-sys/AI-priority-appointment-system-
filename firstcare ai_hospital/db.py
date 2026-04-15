import sqlite3

def get_connection():
    conn = sqlite3.connect("hospital.db")
    conn.row_factory = sqlite3.Row

    # ✅ CREATE TABLE IF NOT EXISTS
    conn.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        symptoms TEXT,
        priority TEXT,
        doctor TEXT,
        suggestion TEXT,
        prescription TEXT,
        status TEXT
    )
    """)

    conn.commit()
    return conn
