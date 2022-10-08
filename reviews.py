from db import db

def get_reviews(material_id):
	sql = """SELECT r.id, u.name, r.rating, r.comment FROM reviews r, users u
             WHERE r.user_id=u.id AND r.material_id=:material_id ORDER BY r.id"""
	return db.session.execute(sql, {"material_id": material_id}).fetchall()

def add_review(material_id, user_id, rating, comment):
	sql = """INSERT INTO reviews (material_id, user_id, rating, comment) VALUES (:material_id, :user_id, :rating, :comment)"""
	db.session.execute(sql, {"material_id":material_id, "user_id":user_id, "rating":rating, "comment":comment})
	db.session.commit()

def delete_review(review_id):
	sql = """DELETE FROM reviews WHERE id=:review_id"""
	db.session.execute(sql, {"review_id":review_id})
	db.session.commit()
