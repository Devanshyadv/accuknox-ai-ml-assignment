import requests
import sqlite3

url = "https://fakerapi.it/api/v1/books?_quantity=10"
response = requests.get(url)

books_data = response.json()["data"]


conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute(
    """
     CREATE TABLE IF NOT EXISTS books(
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     title TEXT,
     author TEXT,
     year TEXT
     )
"""
)


for book in books_data:
    title=book["title"]
    author=book["author"]
    year =book["published"]

    cursor.execute(
        "INSERT INTO books (title, author, year) VALUES (?,?,?)",(title,author,year)
    )

conn.commit()


cursor.execute("SELECT * FROM books")
rows =cursor.fetchall()

print("\n Books stored in database:\n")

for row in rows:
    print(row)


conn.close()