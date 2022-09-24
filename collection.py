from db import db

def add_material(title, author, year, language):
	sql = """INSERT INTO material (title, author, year, language, available) VALUES (:title, :author,:year, :language, TRUE)"""
	db.session.execute(sql, {"title":title, "author":author, "year":year, "language":language})
	db.session.commit()

def get_material_info(material_id):
	sql = """SELECT m.title, m.author, m.year, m.language FROM material m WHERE m.id=:material_id"""
	return db.session.execute(sql, {"material_id": material_id}).fetchone()

def get_all_material():
	sql = "SELECT id, title FROM material ORDER BY title"
	return db.session.execute(sql).fetchall()

def get_new_material():
	sql = "SELECT id, title FROM material ORDER BY id DESC"
	return db.session.execute(sql).fetchmany(5)

def get_material(query):
	sql = "SELECT m.id FROM material m WHERE m.title LIKE :query"
	result = db.session.execute(sql, {"query":"%"+query+"%"})
	result_list = db.session.execute(sql, {"query":"%"+query+"%"}).fetchall()
	if len(result_list) == 0:
		return None
	return db.session.execute(sql, {"query":"%"+query+"%"}).fetchone()[0]
