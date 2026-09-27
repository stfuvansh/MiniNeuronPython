import sqlite3

conn = sqlite3.connect('memory.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS memories (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)')
conn.commit()
def add_memory(content):
    content = content.strip()
    if not content:
        return "Sorry, you didn't enter any memory"
    cursor.execute('INSERT INTO memories (content) VALUES (?)', (content,))
    conn.commit()

def find_memory(query):
    cursor.execute('SELECT * FROM memories WHERE content LIKE ?', ('%' + query + '%',))
    result = cursor.fetchall()
    return result

