create_books_table = """
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_name TEXT NOT NULL,
    author_id INTEGER NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors (id)
)
"""

create_authors_table = """
CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_name TEXT NOT NULL,
    gender TEXT,
    date_of_birth DATE NOT NULL
)
"""

create_readers_table = """
CREATE TABLE IF NOT EXISTS readers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    registration_date DATE NOT NULL,
    favourite_author INTEGER NOT NULL,
    FOREIGN KEY (favourite_author) REFERENCES authors (id)
)
"""

create_orders_table = """
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_date DATE NOT NULL,
    reader_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    FOREIGN KEY (reader_id) REFERENCES readers (id),
    FOREIGN KEY (book_id) REFERENCES books (id)
)
"""

create_authors = """
INSERT INTO authors (author_name, gender, date_of_birth) VALUES 
    ("Александр Сергеевич Пушкин", "MALE", "1799-06-06"),
    ("Фёдор Михайлович Достоевский", "MALE", "1821-10-30"),
    ("Владимир Владимирович Маяковский", "MALE", "1893-07-07"),
    ("Исаак Эммануилович Бабель", "MALE", "1894-06-30"),
    ("Анна Андреевна Ахматова", "FEMALE", "1889-06-23")
"""

create_readers = """
INSERT INTO readers (name, registration_date, favourite_author) VALUES 
    ("Иванов Иван Иванович", 2022-10-10, 1)
"""

