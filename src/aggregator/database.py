import sqlite3

class DatabaseHandler:
    def __init__(self, db_name='content.db'):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()
    

    def create_table(self):
        query = 'CREATE TABLE IF NOT EXISTS content (id INTEGER PRIMARY KEY, data TEXT)'
        self.cursor.execute(query)
        self.connection.commit()
    

    def insert_content(self, data):
        query = 'INSERT INTO content (data) VALUES (?)'
        self.cursor.execute(query, (data,))
        self.connection.commit()

    
    def fetch_all_content(self):
        query = 'SELECT * FROM content'
        self.cursor.execute(query)
        return self.cursor.fetchall()
    

    def close_connection(self):
        self.connection.close()

