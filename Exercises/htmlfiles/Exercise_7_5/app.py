from flask import Flask, render_template, request
import csv
from data_extraction import extraction

app = Flask(__name__)


@app.route("/")
def nav():
    return render_template("base.html")

@app.route("/r1")
def round_1():
    round_db = extraction(mode="round")
    return render_template("round_mean_template.html",Title="Round 1",data_set=round_db[1])

@app.route("/r2")
def round_2():
    round_db = extraction(mode="round")
    return render_template("round_mean_template.html",Title="Round 2",data_set=round_db[2])
    
@app.route("/r3")
def round_3():
    round_db = extraction(mode="round")
    return render_template("round_mean_template.html",Title="Round 3",data_set=round_db[3])
@app.route("/r3")
def round_3():
    round_db = extraction(mode="round")
    return render_template("round_mean_template.html",Title="Round 3",data_set=round_db[3])
    
@app.route("/ms")
def mean_scores():
    mean_scores = extraction(mode="mean")
    return render_template("round_mean_template.html",Title="Mean Scores",data_set=mean_scores)

@app.route("/quals")
def qualifiers():
    qualifiers = extraction(mode="qualifiers")
    return render_template("qualifiers.html", data_set=qualifiers)

@app.route("/query")
def query():
    return render_template("query.html")

@app.route("/query-display", methods=["POST"])
def query_display():
    competitor_id = request.form["query"]
    altered_score_db = extraction(mode="query")
    try:
        competitor_id = int(competitor_id)
        data_set = altered_score_db[competitor_id]
    except:
        data_set = []
    return render_template("query_display.html",data_set=data_set, competitor_id=competitor_id)


if __name__ == "__main__":
    app.run(debug=True)