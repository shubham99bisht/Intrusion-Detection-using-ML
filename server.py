import flask
from flask import Flask, render_template, request, redirect
from eval import main
app = Flask(__name__)

#Basic Web Pages
#-------------------------------------------------------------------------------------------
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/features")
def features():
    return render_template("features.html")

@app.route("/model")
def model():
    return render_template("model.html")

# Web Upload Functions
#-------------------------------------------------------------------------------------------
@app.route("/upload_and_crop", methods=["POST"])
def upload_and_crop():
    if request.method == "POST":
        uid = request.form.get("uid")
        billid = request.form.get("billid")
        result = main(arr)
        return result

# Commands to run
#-------------------------------------------------------------------------------------------
# export FLASK_APP=server.py
# export FLASK_DEBUG=1
# python -m flask run --host 0.0.0.0 --port 5000