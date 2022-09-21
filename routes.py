from app import app
from flask import render_template, request, redirect
import users
import collection


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
		if users.login(username, password):
			return redirect("/")
		else:
			return render_template("error.html", message="Väärä käyttäjätunnus tai salasana")

@app.route("/register", methods=["get", "post"])
def register():
	if request.method == "GET":
		return render_template("register.html")

	if request.method == "POST":
		username = request.form["username"]
		if len(username) < 1 or len(username) > 15:
			return render_template("error.html", message="Käyttätunnuksen tulee olla 1-15 merkkiä pitkä")
		password1 = request.form["password1"]
		password2 = request.form["password2"]
		if password1 != password2:
			return render_template("error.html", message="Salasanat eroavat")
		if password1 == "":
			return render_template("error.html", message="Salasana ei voi olla tyhjä")
		
		role = request.form["role"]
		if role not in ("1", "2"):
			return render_template("error.html", message="Tuntematon käyttäjärooli")
		if not users.register(username, password1, role):
			return render_template("error.html", message="Rekisteröinti ei onnistunut")
		return redirect("/") 

@app.route("/logout")
def logout():
	users.logout()
	return redirect("/")


@app.route("/add", methods=["get", "post"])
def add_material():
	users.require_role(2)

	if request.method == "GET":
		return render_template("add.html")

	if request.method == "POST":
		title = request.form["title"]
		author = request.form["author"]
		year = int(request.form["year"])
		language = request.form["language"]
		
		collection.add_material(title, author, year, language)
		return redirect("/")


