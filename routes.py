from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/login", methods=["get", "post"])
def login():
	if request.method == "GET":
		return render_template("login.html")
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
