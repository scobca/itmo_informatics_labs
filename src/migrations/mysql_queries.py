# creating tables

create_authors_table = """
CREATE TABLE IF NOT EXISTS authors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(255) NOT NULL,
    gender ENUM('MALE', 'FEMALE'),
    date_of_birth DATE NOT NULL
);
"""

create_books_table = """
CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    book_name VARCHAR(255) NOT NULL,
    author_id INT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors (id)
);
"""

create_readers_table = """
CREATE TABLE IF NOT EXISTS readers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    registration_date DATE NOT NULL,
    favourite_author INT NOT NULL,
    FOREIGN KEY (favourite_author) REFERENCES authors (id)
);
"""

create_orders_table = """
CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_date DATE NOT NULL,
    reader_id INT NOT NULL,
    book_id INT NOT NULL,
    FOREIGN KEY (reader_id) REFERENCES readers (id),
    FOREIGN KEY (book_id) REFERENCES books (id)
);
"""

# inserting data

create_authors = """
INSERT INTO authors (author_name, gender, date_of_birth) VALUES 
    ('Александр Сергеевич Пушкин', 'MALE', '1799-06-06'),
    ('Фёдор Михайлович Достоевский', 'MALE', '1821-10-30'),
    ('Владимир Владимирович Маяковский', 'MALE', '1893-07-07'),
    ('Исаак Эммануилович Бабель', 'MALE', '1894-06-30'),
    ('Анна Андреевна Ахматова', 'FEMALE', '1889-06-23');
"""

create_books = """
INSERT INTO books (book_name, author_id) VALUES 
    ('Капитанская дочка', 1),
    ('Братья Карамазовы', 2),
    ('Облако в штанах', 3),
    ('Одесские рассказы', 4),
    ('Реквием', 5);
"""

create_readers = """
INSERT INTO readers (name, registration_date, favourite_author) VALUES 
    ('Иванов Иван Иванович', '2021-03-15', 1),
    ('Алексей Петрович Смирнов', '2023-07-22', 3),
    ('Мария Ивановна Кузнецова', '2024-12-01', 2),
    ('Дмитрий Сергеевич Васильев', '2020-01-15', 5),
    ('Екатерина Андреевна Лебедева', '2021-05-30', 2),
    ('Сергей Николаевич Попов', '2023-03-25', 4),
    ('Анна Владимировна Соколова', '2024-02-14', 3),
    ('Игорь Викторович Михайлов', '2022-10-10', 5);
"""

create_orders = """
INSERT INTO orders (order_date, reader_id, book_id) VALUES
    ('2024-12-08', 1, 5), 
    ('2024-03-15', 2, 4), 
    ('2024-12-31', 3, 3), 
    ('2024-05-20', 4, 2), 
    ('2024-02-29', 5, 1), 
    ('2024-09-10', 4, 1), 
    ('2024-01-01', 2, 4), 
    ('2024-07-04', 3, 2);
"""

# Запрос к бд с использованием join
join_query_get_books = """
SELECT 
    books.book_name,
    authors.author_name 
FROM 
    authors
INNER JOIN books ON books.author_id = authors.id;
"""

# Запрос с использованием where
where_query_get_readers = """
SELECT 
    authors.author_name, COUNT(readers.favourite_author) AS reader_count    
FROM 
    authors
JOIN readers ON authors.id = readers.favourite_author
GROUP BY 
    readers.favourite_author;
"""

# Вложенные запросы
nested_query_1 = """
SELECT 
    readers.name,
    readers.registration_date
FROM 
    readers 
WHERE 
    readers.favourite_author = (
        SELECT id FROM authors WHERE author_name = 'Фёдор Михайлович Достоевский'
);
"""

nested_query_2 = """
SELECT 
    readers.name AS reader_name, 
    books.book_name 
FROM 
    orders 
JOIN readers ON orders.reader_id = readers.id 
JOIN books ON orders.book_id = books.id 
WHERE 
    books.author_id IN (SELECT id FROM authors WHERE date_of_birth > '1850-01-01');
"""

# Union запросы
union_query_1 = """
SELECT name AS name FROM readers
UNION
SELECT author_name AS name FROM authors;
"""

union_query_2 = """
SELECT name AS name FROM readers
UNION
SELECT book_name AS name FROM books;
"""

# Distinct запросы
distinct_query = """
SELECT DISTINCT readers.name FROM readers;
"""

# Updates
update_query_1 = """
UPDATE readers SET name = 'Михайлов Михаил Михайлович' WHERE id = 1;
"""

update_query_2 = """
UPDATE authors SET author_name = 'Фёдор Михайлович Достоевский (обновлённое имя)' WHERE id = 2;
"""

# Delete queries
setting_query = """
    SET FOREIGN_KEY_CHECKS=0;
"""

delete_query_1 = """
DELETE FROM readers WHERE id = 1;
"""

delete_query_2 = """
DELETE FROM authors WHERE id = 1;
"""

delete_query_3 = """
DELETE FROM books WHERE id = 1;
"""

delete_query_4 = """
DELETE FROM orders WHERE id = 1;
"""

delete_all_readers_query = """
DELETE FROM readers;
"""
