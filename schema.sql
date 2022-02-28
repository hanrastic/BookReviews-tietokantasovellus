DROP TABLE IF EXISTS books, books_categories, ratings, reviews CASCADE;

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    is_admin BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    year INTEGER --Year field is optional
);

CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE 
);

CREATE TABLE IF NOT EXISTS books_categories (
	CONSTRAINT book_category_id PRIMARY KEY (book_id, category_id),
	book_id INTEGER REFERENCES books,
	category_id INTEGER REFERENCES categories
);

CREATE TABLE IF NOT EXISTS ratings(
    id SERIAL PRIMARY KEY,
    book_id INTEGER REFERENCES books,
    book_rating INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS reviews (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    book_id INTEGER REFERENCES books,
    created_at TIMESTAMP NOT NULL,
    likes INTEGER,
    rev_comment TEXT
);

