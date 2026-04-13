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

import sqlite3
from dataclasses import dataclass
from datetime import datetime


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


