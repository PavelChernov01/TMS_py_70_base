# Библиотека
# Вы разрабатываете систему для управления библиотекой.
# Необходимо создать базу данных книг, читателей и выдачи книг с помощью SQLite3 и Python-классов.
# 1.	Создайте базу данных library.db, содержащую 3 таблицы:


class Library:  # класс для управления библиотекой

    def __init__(self, db_name='library.db'):
        self.connection = sqlite3.connect(db_name)  # Подключаемся к файлу базы данных
        self.cursor = self.connection.cursor()  # Создаём курсор для выполнения запросов
        self._create_tables()

    def _create_tables(self):  # метод для создания таблиц
        # Создаём таблицу книг
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER,
                status TEXT DEFAULT 'available'
            )
        ''')

        # Создаём таблицу читателей
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS readers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER
            )
        ''')

        # Создаём таблицу выданных книг для связи читателей и книг
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS borrowed_books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                reader_id INTEGER NOT NULL,
                book_id INTEGER NOT NULL,
                borrow_date TEXT NOT NULL
            )
        ''')
        self.connection.commit()  # сохраняем изменения в базе данных

    def add_book(self, title, author, year):  # Метод для добавления новой книги
        self.cursor.execute('''
            INSERT INTO books (title, author, year, status)
            VALUES (?, ?, ?, 'available')
        ''', (title, author, year))
        self.connection.commit()  # Сохраняем изменения
        print(f"Книга '{title}' добавлена")

    def add_reader(self, name, age):  # Метод для добавления нового читателя
        self.cursor.execute('''
            INSERT INTO readers (name, age) VALUES (?, ?)
        ''', (name, age))
        self.connection.commit()  # Сохраняем изменения
        print(f"Читатель '{name}' добавлен")

    def borrow_book(self, reader_id, book_id):  # Метод для выдачи книги читателю
        borrow_date = datetime.now().strftime('%Y-%m-%d')  # Получаем текущую дату
        self.cursor.execute('''
            INSERT INTO borrowed_books (reader_id, book_id, borrow_date)
            VALUES (?, ?, ?)
        ''', (reader_id, book_id, borrow_date))  # Добавляем запись о выдаче
        self.cursor.execute('UPDATE books SET status = "borrowed" WHERE id = ?', (book_id,))  # Меняем статус книги
        self.connection.commit()  # Сохраняем изменения
        print(f"Книга выдана")

    def close(self):  # Метод для закрытия соединения с базой данных
        self.connection.close()  # Закрываем соединение


# Создаём объект библиотеки
library = Library()

# Добавляем несколько книг
library.add_book("Маленький принц", "Антуан де Сент-Экзюпери", 1943)
library.add_book("Война и мир", "Лев Толстой", 1869)

# Добавляем несколько читателей
library.add_reader("Иван Петров", 25)
library.add_reader("Мария Сидорова", 30)

# Выдаём книгу читателю
library.borrow_book(1, 1)

# Закрываем соединение с базой данных
library.close()

# 2.	Используйте dataclass для представления книг и читателей.

from dataclasses import dataclass


# Создаём dataclass для книги
@dataclass
class Book:
    title: str
    author: str
    year: int
    status: str = "available"


# Создаём dataclass для читателя
@dataclass
class Reader:
    name: str
    age: int


class Library:

    def __init__(self, db_name='library.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._create_tables()

    def _create_tables(self):
        # Таблица книг
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER,
                status TEXT DEFAULT 'available'
            )
        ''')

        # Таблица читателей
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS readers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER
            )
        ''')

        # Таблица выданных книг с внешними ключами
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS borrowed_books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                reader_id INTEGER NOT NULL,
                book_id INTEGER NOT NULL,
                borrow_date TEXT NOT NULL,
                FOREIGN KEY (reader_id) REFERENCES readers(id),
                FOREIGN KEY (book_id) REFERENCES books(id)
            )
        ''')
        self.connection.commit()

    def add_book(self, title, author, year):
        new_book = Book(title=title, author=author, year=year)
        self.cursor.execute('''
            INSERT INTO books (title, author, year, status)
            VALUES (?, ?, ?, ?)
        ''', (new_book.title, new_book.author, new_book.year, new_book.status))
        self.connection.commit()
        print(f"Книга '{new_book.title}' добавлена")

    def add_reader(self, name, age):
        new_reader = Reader(name=name, age=age)
        self.cursor.execute('''
            INSERT INTO readers (name, age) VALUES (?, ?)
        ''', (new_reader.name, new_reader.age))
        self.connection.commit()
        print(f"Читатель '{new_reader.name}' добавлен")

    def borrow_book(self, reader_id, book_id):
        borrow_date = datetime.now().strftime('%Y-%m-%d')
        self.cursor.execute('''
            INSERT INTO borrowed_books (reader_id, book_id, borrow_date)
            VALUES (?, ?, ?)
        ''', (reader_id, book_id, borrow_date))
        self.cursor.execute('UPDATE books SET status = "borrowed" WHERE id = ?', (book_id,))
        self.connection.commit()
        print(f"Книга выдана")

    def close(self):
        self.connection.close()


# Создаём объект библиотеки
library = Library()

# Добавляем книги
library.add_book("Маленький принц", "Антуан де Сент-Экзюпери", 1943)
library.add_book("Война и мир", "Лев Толстой", 1869)

# Добавляем читателей
library.add_reader("Иван Петров", 25)
library.add_reader("Мария Сидорова", 30)

# Выдаём книгу
library.borrow_book(1, 1)

# Закрываем библиотеку
library.close()

# 3.	Создать класс Library для работы с базой. Этот класс будет управлять книгами, читателями и выдачей книг.


import sqlite3
from datetime import datetime


class Library:
    def __init__(self, db_name="library.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Создаём таблицу книг
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER,
                status TEXT DEFAULT 'available'
            )
        ''')

        # Создаём таблицу читателей
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS readers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER
            )
        ''')

        # Создаём таблицу выданных книг
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS borrowed_books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                reader_id INTEGER NOT NULL,
                book_id INTEGER NOT NULL,
                borrow_date TEXT NOT NULL,
                FOREIGN KEY (reader_id) REFERENCES readers(id),
                FOREIGN KEY (book_id) REFERENCES books(id)
            )
        ''')
        self.conn.commit()
        # Таблицы готовы к работе

    def add_book(self, title, author, year):
        self.cursor.execute('''
            INSERT INTO books (title, author, year, status)
            VALUES (?, ?, ?, 'available')
        ''', (title, author, year))
        self.conn.commit()
        # Книга добавлена в базу данных

    def add_reader(self, name, age):
        self.cursor.execute('''
            INSERT INTO readers (name, age) VALUES (?, ?)
        ''', (name, age))
        self.conn.commit()
        # Читатель добавлен в базу данных

    def borrow_book(self, reader_id, book_id):
        # Проверяем существует ли книга и свободна ли она
        self.cursor.execute('SELECT title, status FROM books WHERE id = ?', (book_id,))
        book = self.cursor.fetchone()

        if not book:
            print("Книга не найдена")
            return False

        if book[1] == 'borrowed':
            print(f"Книга '{book[0]}' уже выдана")
            return False

        # Проверяем существует ли читатель
        self.cursor.execute('SELECT name FROM readers WHERE id = ?', (reader_id,))
        reader = self.cursor.fetchone()

        if not reader:
            print("Читатель не найден")
            return False

        # Записываем выдачу книги и меняем её статус
        borrow_date = datetime.now().strftime('%Y-%m-%d')

        self.cursor.execute('''
            INSERT INTO borrowed_books (reader_id, book_id, borrow_date)
            VALUES (?, ?, ?)
        ''', (reader_id, book_id, borrow_date))

        self.cursor.execute('UPDATE books SET status = "borrowed" WHERE id = ?', (book_id,))
        self.conn.commit()

        print(f"Книга '{book[0]}' выдана читателю '{reader[0]}'")
        return True

    def return_book(self, book_id):
        # Проверяем существует ли книга и выдана ли она
        self.cursor.execute('SELECT title, status FROM books WHERE id = ?', (book_id,))
        book = self.cursor.fetchone()

        if not book:
            print("Книга не найдена")
            return False

        if book[1] == 'available':
            print(f"Книга '{book[0]}' уже в библиотеке")
            return False

        # Возвращаем книгу и удаляем запись о выдаче
        self.cursor.execute('UPDATE books SET status = "available" WHERE id = ?', (book_id,))
        self.cursor.execute('DELETE FROM borrowed_books WHERE book_id = ?', (book_id,))
        self.conn.commit()

        print(f"Книга '{book[0]}' возвращена")
        return True

    def search_books(self, keyword):
        # Ищем книги по названию или автору
        self.cursor.execute('''
            SELECT id, title, author, year, status 
            FROM books 
            WHERE title LIKE ? OR author LIKE ?
        ''', (f'%{keyword}%', f'%{keyword}%'))

        results = self.cursor.fetchall()

        if not results:
            print(f"По запросу '{keyword}' ничего не найдено")
            return []

        print(f"\nРезультаты поиска '{keyword}':")
        for book in results:
            status = "Доступна" if book[4] == 'available' else "Выдана"
            print(f"id:{book[0]} | {book[1]} | {book[2]} | {book[3]} | {status}")

        return results

    def get_borrowed_books(self):
        # Получаем список всех выданных книг с именами читателей
        self.cursor.execute('''
            SELECT readers.name, books.title, books.author, borrowed_books.borrow_date
            FROM borrowed_books
            JOIN readers ON borrowed_books.reader_id = readers.id
            JOIN books ON borrowed_books.book_id = books.id
        ''')

        results = self.cursor.fetchall()

        if not results:
            print("Нет выданных книг")
            return []

        print("\nСписок выданных книг:")
        for item in results:
            print(f"Читатель: {item[0]} | Книга: {item[1]} | Автор: {item[2]} | Дата: {item[3]}")

        return results

    def get_statistics(self):
        # Считаем количество доступных книг
        self.cursor.execute('SELECT COUNT(*) FROM books WHERE status = "available"')
        available = self.cursor.fetchone()[0]

        # Считаем количество выданных книг
        self.cursor.execute('SELECT COUNT(*) FROM books WHERE status = "borrowed"')
        borrowed = self.cursor.fetchone()[0]

        # Считаем общее количество книг
        self.cursor.execute('SELECT COUNT(*) FROM books')
        total = self.cursor.fetchone()[0]

        # Выводим статистику
        print("\nСтатистика библиотеки:")
        print(f"Всего книг: {total}")
        print(f"Доступно: {available}")
        print(f"Выдано: {borrowed}")


# Создаём библиотеку
library = Library()

# Добавляем книги
library.add_book("Маленький принц", "Антуан де Сент-Экзюпери", 1943)
library.add_book("Война и мир", "Лев Толстой", 1869)

# Добавляем читателей
library.add_reader("Иван Петров", 25)
library.add_reader("Мария Сидорова", 30)

# Выдаём книгу читателю
library.borrow_book(1, 1)

# Показываем список выданных книг
library.get_borrowed_books()

# Показываем статистику библиотеки
library.get_statistics()

# Закрываем соединение с базой данных
library.conn.close()