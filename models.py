import sqlite3

def connect():
    return sqlite3.connect("database.db")

def create_tables():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS assets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        ticker TEXT,
        sector TEXT,
        market TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS metrics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        asset_id INTEGER,
        pl REAL,
        roe REAL,
        dy REAL,
        debt REAL,
        growth REAL,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()