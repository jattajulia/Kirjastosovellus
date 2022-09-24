from db import db

def make_reservation(material_id, user_id):
	sql = """INSERT INTO reservations (user_id, material_id) VALUES (:material_id, :user_id)"""
	db.session.execute(sql, {"material_id":material_id, "user_id":user_id})
	db.session.commit()

def get_reservations(material_id):
	sql = """SELECT COUNT(*) FROM reservations r WHERE r.id=:material_id"""
	return db.session.execute(sql, {"material_id": material_id}).fetchone()[0]
