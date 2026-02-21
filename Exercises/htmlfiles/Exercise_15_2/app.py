from flask import Flask,render_template,request
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/query',methods=["POST","GET"])
def query():
    brand = request.form.get("brand")
    try:
        client = MongoClient("localhost",27017)
        print("Connect successfully")
    except:
        print("Failed to connect to client")

    db = client["Exercise_15_2(jp_mobile)"]
    coll = db["phone"]
    data = [[i["brand"],i["model"],i["colour"],i["price"],i["quantity"]] for i in list(coll.find({"brand":brand}))]
    return render_template("query.html",data=data)


if __name__ == "__main__":
    app.run(debug=True)