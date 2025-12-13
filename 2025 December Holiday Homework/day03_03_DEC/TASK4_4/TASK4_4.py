from flask import Flask, render_template, redirect, url_for,request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/query',methods=["POST"])
def query():
    Comp_ID = request.form["Comp_ID"]
    conn = sqlite3.connect("../resources/club.db")
    cursor = conn.cursor()

    cursor.execute("SELECT m.Mem_Name, m.Mem_ID, s.Comp_Score FROM Scores s JOIN Members m ON s.Mem_ID = m.Mem_ID WHERE s.Comp_ID = ?",(Comp_ID,))
    query = cursor.fetchall()
    return render_template("index.html",data=query)


if __name__ == "__main__":
    app.run(debug=True)