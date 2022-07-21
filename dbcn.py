from pandas import DataFrame
import sqlite3

def racks():

    db = "database.db"
    conn = None
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    d1 = cur.execute("SELECT * FROM racks;")
    df1 = DataFrame(d1.fetchall())
    return df1
