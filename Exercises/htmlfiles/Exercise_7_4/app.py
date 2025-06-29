from flask import render_template, Flask
import csv


app=Flask(__name__)

human_db = {}
with open("../resources/people.txt") as data:
    reader = csv.reader(data)
    for human in reader:
        if human[-1] not in human_db.keys():
            human_db[human[-1]]=[human[0:2]]
        else:
            current = human_db.get(human[-1])
            current.append(human[0:2])
        

@app.route("/")
def index():
    return render_template("base.html",human_db=human_db)


if __name__ == "__main__":
    app.run(debug=True)