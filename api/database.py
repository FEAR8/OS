import sqlite3
import os


#Create and connnet database
conn = sqlite3.connect('nexus.db')
cur = conn.cursor()

sql_database = '''
     CREATE TABLE IF NOT EXISTS data (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     temp_value REAL NOT NULL,
     hum_value REAL NULL,
     status BOOLEAN DEFAULT TRUE,
     create_at TIMESTAMP DEFAULT (datetime('now','localtime'))

     );
'''
cur.execute(sql_database)
conn.commit()
conn.close()