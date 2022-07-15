import sqlite3


conn = sqlite3.connect("shorty.db")
cursor = conn.cursor()


cursor.execute("DELETE FROM short_urls WHERE created_at < DATETIME('now', '-30 days', '239 minute', '52 seconds')")
conn.commit()



