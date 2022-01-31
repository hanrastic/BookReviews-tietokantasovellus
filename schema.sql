DROP TABLE IF EXISTS books, categories, books_categories, ratings, reviews CASCADE;

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    is_admin BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    year INTEGER NOT NULL,
);

CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE 
);

CREATE TABLE books_categories (
	CONSTRAINT book_category_id PRIMARY KEY (book_id, category_id),
	book_id INTEGER REFERENCES books ON UPDATE CASCADE,
	category_id INTEGER REFERENCES categories ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS ratings(
    id SERIAL PRIMARY KEY,
    book_id INTEGER REFERENCES books,
    rating NUMERIC NOT NULL
);

CREATE TABLE IF NOT EXISTS reviews (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    book_id INTEGER REFERENCES books,
    category_id INTEGER REFERENCES categories,
    rating_id INTEGER REFERENCES ratings,
    created_at TIMESTAMP NOT NULL,
    likes INTEGER,
    comment TEXT NOT NULL
);







-- CREATE TABLE readingList(
--     id SERIAL PRIMARY KEY,
--     user_id INTEGER REFERENCES users,
--     book_name INTEGER REFERENCES books
--     read_status BOOLEAN
-- );

