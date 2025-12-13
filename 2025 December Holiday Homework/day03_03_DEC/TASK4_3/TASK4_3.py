from flask import Flask, render_template,redirect,url_for,request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/query',methods=["POST"])
def query():
    print(request.form.keys())
    Mem_ID = request.form["Mem_ID"]
    Comp_ID = request.form["Comp_ID"]
    Comp_Score = request.form["Comp_Score"]

    conn = sqlite3.connect("../resources/club.db")
    scores_query = "INSERT INTO Scores(Mem_ID,Comp_ID,Comp_Score) VALUES(?,?,?)"
    conn.execute(scores_query,(Mem_ID,Comp_ID,Comp_Score))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)