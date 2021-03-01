import sqlite3

def connect():
    conn = sqlite3.connect('passwords.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS passwords(id INTEGER PRIMARY KEY, account, password)')
    conn.commit()
    conn.close()


def insert(account, password):
    conn = sqlite3.connect('passwords.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO passwords VALUES(NULL,?,?)', (account, password))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('passwords.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM passwords')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def search(account='', password=''):
    conn = sqlite3.connect('passwords.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM passwords WHERE account=? or password=?',(account, password))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows
def delete(id):
    conn = sqlite3.connect('passwords.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM passwords WHERE id=?',(id,))
    conn.commit()
    conn.close()


def update(id, account, password):
    conn = sqlite3.connect('passwords.db')
    cur = conn.cursor()
    cur.execute('UPDATE passwords SET account=?, password=? WHERE id=?',(account, password, id))
    conn.commit()
    conn.close()


connect()


