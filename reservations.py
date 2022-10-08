from db import db

def make_reservation(material_id, user_id):
	sql = """INSERT INTO reservations (user_id, material_id) VALUES (:user_id, :material_id)"""
	db.session.execute(sql, {"user_id":user_id, "material_id":material_id})
	db.session.commit()

def get_reservations(material_id):
	sql = """SELECT COUNT(*) FROM reservations r WHERE r.material_id=:material_id"""
	return db.session.execute(sql, {"material_id": material_id}).fetchone()[0]

def get_user_reservations(user_id):
	sql = """SELECT m.id, m.title FROM material m, reservations r WHERE r.material_id=m.id AND r.user_id=:user_id"""
	return db.session.execute(sql, {"user_id": user_id}).fetchall()

def get_most_reserved():
	sql = """SELECT m.id, m.title, (SELECT COUNT(*) FROM reservations r WHERE r.material_id = m.id) count  FROM material m ORDER BY count DESC"""
	return db.session.execute(sql).fetchmany(5)

