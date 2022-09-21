from db import db

def add_material(title, author, year, language):
	sql = """INSERT INTO material (title, author, year, language, available) VALUES (:title, :author,:year, :language, TRUE)"""
	db.session.execute(sql, {"title":title, "author":author, "year":year, "language":language})
	db.session.commit()
