from app import app
from flask import render_template, request, redirect
import users
import collection
import reservations
from db import db


@app.route("/")
def index():
	return render_template("index.html", collection=collection.get_new_material())

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

@app.route("/reservation/<int:material_id>", methods=["get"])
def make_reservation(material_id):
	user_id = users.user_id()
	reservations.make_reservation(material_id, user_id)
	return redirect("/material/"+str(material_id))
	


@app.route("/search", methods=["get"])
def search():
	if request.method == "GET":
		return render_template("search.html")
		

@app.route("/result")
def result():
	query = request.args["query"]
	material_id = collection.get_material(query)
	if material_id is None:
		return render_template("error.html", message="Haullasi ei löytynyt aineistoa")
	return redirect("/material/"+str(material_id))

@app.route("/material/<int:material_id>")
def show_material(material_id):
	info = collection.get_material_info(material_id)
	reservation_count = reservations.get_reservations(material_id)
	return render_template("material.html", id=material_id, title=info[0], author=info[1], year=info[2], language=info[3], reservations=reservation_count)

