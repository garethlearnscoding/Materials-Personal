from flask import Flask, render_template


app = Flask(__name__)

color_dict = {"000":"red","001":"white","010":"yellow","011":"blue","100":"black","110":"green"}
with open("../resources/decompressedimage.txt") as f:
    data = [color_dict[i.strip()] for i in f.readlines()]
    rows = [data[j:j+9] for j in range(0,len(data),9)]
    
@app.route('/')
def index():
    return render_template("index.html",data = rows)


if __name__ == "__main__":
    app.run(debug=True)