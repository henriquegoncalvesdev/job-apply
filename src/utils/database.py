import sqlite3

class Database:
    def __init__(self, db_path='job_apply.db'):
        self.conn = sqlite3.connect(db_path)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS applications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_url TEXT,
                status TEXT,
                applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()

    def log_application(self, job_url, status):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO applications (job_url, status) VALUES (?, ?)', (job_url, status))
        self.conn.commit()
