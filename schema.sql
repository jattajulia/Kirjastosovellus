CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	name TEXT,
	password TEXT,
	role INTEGER
);

CREATE TABLE material (
	id SERIAL PRIMARY KEY,
	title TEXT,
	author TEXT,
	year INTEGER,
	language TEXT,
	available BOOLEAN
);

CREATE TABLE reservations (
	id SERIAL PRIMARY KEY,
	user_id INTEGER REFERENCES users,
	material_id INTEGER REFERENCES material
);

CREATE TABLE borrowing_privileges (
	id SERIAL PRIMARY KEY,
	user_id INTEGER REFERENCES users,
	suspended BOOLEAN
);

CREATE TABLE reviews (
	id SERIAL PRIMARY KEY,
	user_id INTEGER REFERENCES users,
	material_id INTEGER REFERENCES material,
	rating INTEGER,
	comment TEXT
);
