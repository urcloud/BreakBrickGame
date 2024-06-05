import sqlite3

def create_table():
    conn = sqlite3.connect('game_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 score INTEGER NOT NULL,
                 level INTEGER NOT NULL
                 )''')
    conn.commit()
    conn.close()

def save_user_data(name, score, level):
    conn = sqlite3.connect('game_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, score, level) VALUES (?, ?, ?)",
               (name, score, level))
    conn.commit()
    conn.close()

def get_top_scores():
    conn = sqlite3.connect('game_data.db')
    c = conn.cursor()
    c.execute("SELECT name, score FROM users ORDER BY score DESC LIMIT 3")
    top_scores = c.fetchall()
    conn.close()
    if not top_scores:
        return []
    return top_scores