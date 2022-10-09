from app import app
from flask import render_template, request, redirect
import users
import collection
import reservations
import reviews
from db import db


@app.route("/")
def index():
	return render_template("index.html", collection=collection.get_new_material(), topreserved=reservations.get_most_reserved())

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
		try:
			year = int(request.form["year"])
		except:
			return render_template("error.html", message="Vuosiluku on annettava numeroina")
		language = request.form["language"]
		if len(title) < 1 or len(author) < 1 or len(language) < 1:
			return render_template("error.html", message="Et voi jättää kenttiä tyhjiksi")
		collection.add_material(title, author, year, language)
		return redirect("/")

@app.route("/reservation/<int:material_id>", methods=["get"])
def make_reservation(material_id):
	user_id = users.user_id()
	if users.is_suspended(user_id):
		return render_template("error.html", message="Et voi varata teosta, koska sinulla ei ole lainausoikeuksia")
	reservation_list = reservations.get_user_reservations(user_id)
	for i in reservation_list:
		if i[0] == material_id:
			return 	render_template("error.html", message="Olet jo varannut tämän teoksen")
	reservations.make_reservation(material_id, user_id)
	collection.change_availability(material_id)
	reservation_title = collection.get_material_title(material_id)[1]
	return render_template("reservation.html", title = reservation_title)
	


@app.route("/search", methods=["get"])
def search():
	if request.method == "GET":
		return render_template("search.html")
		

@app.route("/result")
def result():
	query = request.args["query"]
	material_list = collection.get_material(query)
	if material_list is None:
		return render_template("error.html", message="Haullasi ei löytynyt aineistoa")
	return render_template("result.html", search_results = material_list)

@app.route("/material/<int:material_id>")
def show_material(material_id):
	info = collection.get_material_info(material_id)
	if collection.get_material_availability(material_id):
		available = "Kyllä"
	else:
		available = "Ei"
	reservation_count = reservations.get_reservations(material_id)
	review_list = reviews.get_reviews(material_id)
	if review_list:
		review_count = len(review_list)
	else:
		review_count = 0
	return render_template("material.html", id=material_id, title=info[0], author=info[1], year=info[2], language=info[3], reservations=reservation_count, available=available, review_list=review_list, review_count=review_count)

@app.route("/userreservations")
def myreservations():
	user_id = users.user_id()
	reservation_list = reservations.get_user_reservations(user_id)
	return render_template("user_reservations.html", lista = reservation_list)

@app.route("/review", methods=["post"])
def review():
	users.require_role(1)
	material_id = request.form["material_id"]
	rating = int(request.form["rating"])
	if rating < 1 or rating > 5:
        	return render_template("error.html", message="Virheellinen arvosana")
	comment = request.form["comment"]
	if len(comment) > 1000:
		return render_template("error.html", message="Kommentti on liian pitkä")
	if comment == "":
		comment = "-"
	reviews.add_review(material_id, users.user_id(), rating, comment)
	return redirect("/material/"+str(material_id))

@app.route("/delete_review/<review_id>", methods=['POST'])
def delete_review(review_id):
	reviews.delete_review(review_id)
	return render_template("verification.html", message="Kommentti poistettiin")

@app.route("/delete_material/<material_id>", methods=['POST'])
def delete_material(material_id):
	collection.delete_material(material_id)
	return render_template("verification.html", message="Aineisto poistettiin")
	

@app.route("/admin", methods=["get", "post"])
def control_privileges():
	if request.method == "GET":
		return render_template("borrowing_privileges.html")
	if request.method == "POST":
		username = request.form["name"]
		if users.disable_borrowing(username):
			return render_template("verification.html", message="Käyttäjän lainausoikeus poistettiin")
		else:
			return render_template("error.html", message="Käyttäjänimeä ei löydy")
	


