from flask import Flask, render_template,redirect,request,url_for
import sqlite3


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("TASK4_2.html")


@app.route('/display')
def display():
    con = sqlite3.connect("../../resources/Task4.db")
    c = con.cursor()

    c.execute("SELECT b.bookID,b.title,b.price,COUNT(c.copyID) FROM books b LEFT JOIN copies c ON b.bookID == c.bookID GROUP BY b.bookID ORDER BY b.bookID")
    info = c.fetchall()
    return render_template("TASK4_4.html",data=info)

@app.route('/insert')
def insert():
    return render_template('TASK4_3.html')

@app.route('/insert-query',methods=["POST"])
def insert_query():
    bookID = request.form["BookID"]
    title = request.form["title"]
    price = request.form["price"]
    copies = request.form["copies"]

    books_data = (bookID,title,price)
    copies_data = [(f"{i+1:04}",bookID) for i in range(int(copies))]
    con = sqlite3.connect("../../resources/Task4.db")
    c = con.cursor()

    c.execute("INSERT INTO books(bookID,title,price) VALUES (?,?,?)",books_data)
    c.executemany("INSERT INTO copies(copyID,bookID) VALUES (?,?)",copies_data)

    con.commit()
    con.close()

    return redirect(url_for('insert'))


if __name__ == "__main__":
    app.run(debug=True)