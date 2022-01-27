CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT,
    isAdmin INTEGER
);

CREATE TABLE books(
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    year INTEGER,
    rating NUMERIC REFERENCES ratings, --????? Tämä ei ihan selkeä
    category TEXT REFERENCES categories,
);

CREATE TABLE reviews(
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    book_id INTEGER REFERENCES books,
    category_id INTEGER REFERENCES categories,
    createdAt TIMESTAMP,
    likes INTEGER,
    comment TEXT
);

CREATE TABLE categories(
    id SERIAL PRIMARY KEY,
    book_id REFERENCES books,
    name TEXT UNIQUE 
);

CREATE TABLE ratings(
    id SERIAL PRIMARY KEY,
    book_id INTEGER REFERENCES books,
    rating NUMERIC
);

CREATE TABLE readingList(
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    bookName TEXT REFERENCES books
    readStatus BOOLEAN
);

