from db import db

def add_material(title, author, year, language):
	sql = """INSERT INTO material (title, author, year, language, available) VALUES (:title, :author,:year, :language, TRUE)"""
	db.session.execute(sql, {"title":title, "author":author, "year":year, "language":language})
	db.session.commit()

def get_material_info(material_id):
	sql = """SELECT m.title, m.author, m.year, m.language FROM material m WHERE m.id=:material_id"""
	return db.session.execute(sql, {"material_id": material_id}).fetchone()

def get_material_title(material_id):
	sql = """SELECT m.id, m.title FROM material m WHERE m.id=:material_id"""
	return db.session.execute(sql, {"material_id": material_id}).fetchone()

def get_all_material():
	sql = "SELECT id, title FROM material ORDER BY title"
	return db.session.execute(sql).fetchall()

def get_new_material():
	sql = "SELECT id, title FROM material ORDER BY id DESC"
	return db.session.execute(sql).fetchmany(5)

def get_material(query):
	sql = "SELECT id, title FROM material WHERE title LIKE :query OR language LIKE :query OR author LIKE :query"
	result = db.session.execute(sql, {"query":"%"+query+"%"})
	result_list = db.session.execute(sql, {"query":"%"+query+"%"}).fetchall()
	if len(result_list) == 0:
		return None
	return db.session.execute(sql, {"query":"%"+query+"%"}).fetchall()

def get_reviews(material_id):
	sql = """SELECT u.name, r.rating, r.comment FROM reviews r, users u
             WHERE r.user_id=u.id AND r.material_id=:material_id ORDER BY r.id"""
	return db.session.execute(sql, {"material_id": material_id}).fetchall()

def add_review(material_id, user_id, rating, comment):
	sql = """INSERT INTO reviews (material_id, user_id, rating, comment) VALUES (:material_id, :user_id, :rating, :comment)"""
	db.session.execute(sql, {"material_id":material_id, "user_id":user_id, "rating":rating, "comment":comment})
	db.session.commit()
