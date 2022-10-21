from db import db

def add_material(title, author, year, language):
	sql = """INSERT INTO material (title, author, year, language, available) VALUES (:title, :author,:year, :language, TRUE)"""
	db.session.execute(sql, {"title":title, "author":author, "year":year, "language":language})
	db.session.commit()

def delete_material(material_id):
	sql = """DELETE FROM material WHERE id=:material_id"""
	db.session.execute(sql, {"material_id": material_id})
	db.session.commit()

def get_material_info(material_id):
	sql = """SELECT m.title, m.author, m.year, m.language FROM material m WHERE m.id=:material_id"""
	return db.session.execute(sql, {"material_id": material_id}).fetchone()

def get_material_title(material_id):
	sql = """SELECT m.id, m.title FROM material m WHERE m.id=:material_id"""
	return db.session.execute(sql, {"material_id": material_id}).fetchone()

def get_all_material():
	sql = """SELECT id, title FROM material ORDER BY title"""
	return db.session.execute(sql).fetchall()

def change_availability(material_id):
	sql = """UPDATE material SET available=FALSE WHERE id=:material_id"""
	db.session.execute(sql, {"material_id": material_id})
	db.session.commit()

def get_new_material():
	sql = """SELECT id, title FROM material ORDER BY id DESC"""
	return db.session.execute(sql).fetchmany(5)

def get_material_availability(material_id):
	sql = """SELECT m.available FROM material m WHERE m.id=:material_id"""
	return db.session.execute(sql, {"material_id": material_id}).fetchone()[0]

def get_material_by_title(query):
	sql = """SELECT id, title FROM material WHERE title LIKE :query"""
	result = db.session.execute(sql, {"query":"%"+query+"%"})
	result_list = db.session.execute(sql, {"query":"%"+query+"%"}).fetchall()
	if len(result_list) == 0:
		return None
	return db.session.execute(sql, {"query":"%"+query+"%"}).fetchall()

def get_material_by_author(query):
	sql = """SELECT id, title FROM material WHERE author LIKE :query"""
	result = db.session.execute(sql, {"query":"%"+query+"%"})
	result_list = db.session.execute(sql, {"query":"%"+query+"%"}).fetchall()
	if len(result_list) == 0:
		return None
	return db.session.execute(sql, {"query":"%"+query+"%"}).fetchall()

def get_material_by_language(query):
	sql = """SELECT id, title FROM material WHERE language LIKE :query"""
	result = db.session.execute(sql, {"query":"%"+query+"%"})
	result_list = db.session.execute(sql, {"query":"%"+query+"%"}).fetchall()
	if len(result_list) == 0:
		return None
	return db.session.execute(sql, {"query":"%"+query+"%"}).fetchall()



