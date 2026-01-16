import sqlite3
import csv

conn =sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
      CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               email TEXT
               
               )
""")

with open("names_emails.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?,?) ",
            (row["Name"],row["Email"])
        )

conn.commit()

cursor.execute("SELECT * FROM users LIMIT 10")
rows = cursor.fetchall()

print("\nUsers stored in database:\n")
for row in rows:
    print(row)


conn.close()
