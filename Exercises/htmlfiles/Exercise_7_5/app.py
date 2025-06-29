from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def nav():
    return render_template("base.html")

@app.route("/r1")
def round_1():
    return render_template("round_1.html")

@app.route("/r2")
def round_2():
    return render_template("round_2.html")
    
@app.route("/r3")
def round_3():
    return render_template("round_3.html")
    
@app.route("/ms")
def round_3():
    return render_template("mean_scores.html")

@app.route("/quals")
def round_3():
    return render_template("qualifiers.html")






if __name__ == "__main__":
    app.run(debug=True)