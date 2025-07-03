import sqlite3

# Connect to database (auto-creates if not exist)
def connect_db():
    return sqlite3.connect("expenses.db")

# Create required tables
def create_tables():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            date TEXT,
            category TEXT,
            description TEXT,
            amount REAL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')

    conn.commit()
    conn.close()

# Register a new user
def register_user(username, password):
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False

# Login user
def login_user(username, password):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = cur.fetchone()
    conn.close()
    return result

# Add new expense
def add_expense(user_id, date, category, description, amount):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO expenses (user_id, date, category, description, amount) VALUES (?, ?, ?, ?, ?)",
        (user_id, date, category, description, amount)
    )
    conn.commit()
    conn.close()

# Get all expenses for a user
def get_expenses(user_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT date, category, description, amount FROM expenses WHERE user_id=?", (user_id,))
    rows = cur.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    create_tables()
    print("Tables created successfully.")