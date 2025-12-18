import sqlite3
import csv
with open('../resources/books_data.txt') as f:
    books_data = [tuple(i) for i in list(csv.reader(f))]

with open('../resources/copies_data.txt') as f:
    copies_data = [tuple(i[:2:]) for i in list(csv.reader(f))]

books_query = "INSERT INTO books(bookID,title,price) VALUES (?,?,?)"
copies_query = "INSERT INTO copies(copyID,bookID) VALUES (?,?)"

con = sqlite3.connect("../resources/Task4.db")
c = con.cursor()

c.executemany(books_query,books_data)
c.executemany(copies_query,copies_data)

con.commit()
con.close()