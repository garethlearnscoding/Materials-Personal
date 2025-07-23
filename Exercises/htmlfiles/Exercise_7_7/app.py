from flask import Flask, render_template, request, redirect
from util.compress import read_decompress, compress_data, write_compress
from util.decompress import read_compress, decompress_data, write_decompress
import os

app = Flask(__name__)

@app.route("/")
def nav():
    error = request.args["error"]
    match error:
        
    return render_template("base.html")

@app.route("/processing", methods=["POST"])
def processing():
    file_name = request.form["filename"]
    process = request.form["process"]
    print(process)
    folder = "assets"
    file_path = f"./{folder}/{file_name}"
    try:
        with open(file_path) as check:
            pass
        print(f"File Found: {file_path}")
        if int(process):
            data = read_compress(file_name,folder)
            print(f"Data: {data}")
            decompressed_data = decompress_data(data)
            print(f"Decompressed_data: {decompressed_data}")
            if write_decompress(decompressed_data,folder):
                return render_template("base.html",error_data=True)
        else:
            data = read_decompress(file_name,folder)
            compressed_data = compress_data(data)
            if status := write_compress(compressed_data,folder):
                return render_template("base.html",error_data=True)

    except FileNotFoundError:
        return redirct(url_for("nav",error="error_file"))
    else:
        return redirect("/")

if __name__=="__main__":
    app.run(debug=True)

