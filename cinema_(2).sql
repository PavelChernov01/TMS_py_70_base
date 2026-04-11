DROP TABLE IF EXISTS actors_movies;
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS bank_accounts;
DROP TABLE IF EXISTS actors;
DROP TABLE IF EXISTS director;

-- 1. Создать таблицы с данными согласно спроектированной схеме. Заполнить предоставленными данными.

CREATE TABLE actors (
    actors_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    age INTEGER,
    sex TEXT CHECK (sex IN ('m', 'f'))
);

INSERT INTO actors (actors_id, name, surname, age, sex) VALUES
(1, 'Arnold', 'Schwarzenegger', 75, 'm'),
(2, 'Bruce', 'Willis', 67, 'm'),
(3, 'Tom', 'Cruise', 60, 'm'),
(4, 'Brad', 'Pitt', 53, 'm'),
(5, 'Will', 'Smith', 54, 'm'),
(6, 'Leonardo', 'DiCaprio', 48, 'm'),
(7, 'Tom', 'Hanks', 66, 'm'),
(8, 'Johnny', 'Depp', 59, 'm'),
(9, 'Harrison', 'Ford', 80, 'm'),
(10, 'Sandra', 'Bullock', 58, 'f'),
(11, 'Halle', 'Berry', 56, 'f'),
(12, 'Julia', 'Roberts', 55, 'f'),
(13, 'Kate', 'Winslet', 47, 'f'),
(14, 'Angelina', 'Jolie', 47, 'f');

-- Таблица director
DROP TABLE IF EXISTS director;
CREATE TABLE director (
    director_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    age INTEGER,
    sex TEXT CHECK (sex IN ('m', 'f'))
);

INSERT INTO director (director_id, name, surname, age, sex) VALUES
(1, 'James', 'Cameron', 68, 'm'),
(2, 'Steven', 'Spilberg', 75, 'm'),
(3, 'Robert', 'Zemeckis', 70, 'm'),
(4, 'Doug', 'Liman', 57, 'm'),
(5, 'Brian', 'De Palma', 82, 'm'),
(6, 'John', 'Woo', 76, 'm'),
(7, 'Tim', 'Berton', 64, 'm'),
(8, 'Jan', 'De Bont', 79, 'm'),
(9, 'Alejandro', 'Agresti', 61, 'm'),
(10, 'Garry', 'Marshal', 82, 'm'),
(11, 'Steven', 'Sodeberg', 59, 'm'),
(12, 'Michael', 'Bay', 57, 'm'),
(13, 'Barry', 'Sonnenfeld', 69, 'm'),
(14, 'Simon', 'Kinberg', 49, 'm'),
(15, 'Christopher', 'Nolan', 52, 'm'),
(16, 'Martin', 'Scorsese', 80, 'm'),
(17, 'Stanley', 'Kubrick', 70, 'm'),
(18, 'Woody', 'Allen', 87, 'm');

-- Таблица movies
DROP TABLE IF EXISTS movies;
CREATE TABLE movies (
    movie_id INTEGER PRIMARY KEY,
    name_movie TEXT NOT NULL,
    release INTEGER,
    budjet INTEGER,
    director_id INTEGER,
    FOREIGN KEY (director_id) REFERENCES director(director_id)
);

INSERT INTO movies (movie_id, name_movie, release, budjet, director_id) VALUES
(1, 'Titanic', 1997, 200000000, 1),
(2, 'Catch me if you can', 2002, 52000000, 2),
(3, 'Forrest Gump', 1994, 55000000, 3),
(4, 'Terminator 2', 1991, 102000000, 1),
(5, 'Mr. & Mrs. Smith', 2005, 110000000, 4),
(6, 'Indiana Jones 3', 1989, 48000000, 2),
(7, 'Mission impossible 1', 1996, 80000000, 5),
(8, 'Mission impossible 2', 2000, 125000000, 6),
(9, 'Charlie and the Chocolate Factory', 2005, 150000000, 7),
(10, 'Speed', 1994, 25000000, 8),
(11, 'Lake House', 2006, 40000000, 9),
(12, 'Pretty women', 1990, 190000000, 10),
(13, 'Ocean''s eleven', 2001, 184000000, 11),
(14, 'Larry Crowne', 2011, 30000000, NULL),
(15, 'Bad boys 1', 1995, 19000000, 12),
(16, 'Bad boys 2', 2003, 130000000, 12),
(17, 'Men in black', 1997, 90000000, 13),
(18, 'The Martian', 2015, 108000000, 14),
(19, 'Interstellar', 2014, 165000000, 15);

-- Таблица actors_movies
DROP TABLE IF EXISTS actors_movies;
CREATE TABLE actors_movies (
    actors_movies_id INTEGER PRIMARY KEY,
    movies_id INTEGER,
    actors_id INTEGER,
    FOREIGN KEY (movies_id) REFERENCES movies(movie_id),
    FOREIGN KEY (actors_id) REFERENCES actors(actors_id)
);

INSERT INTO actors_movies (actors_movies_id, movies_id, actors_id) VALUES
(1, 1, 6),
(2, 1, 13),
(3, 2, 6),
(4, 2, 7),
(5, 3, 7),
(6, 4, 1),
(7, 5, 4),
(8, 5, 14),
(9, 6, 9),
(10, 7, 3),
(11, 8, 3),
(12, 9, 8),
(13, 10, 10),
(14, 11, 10),
(15, 12, 12),
(16, 13, 4),
(17, 13, 12),
(18, 14, 7),
(19, 14, 12),
(20, 15, 5),
(21, 16, 5),
(22, 17, 5),
(23, 18, NULL),
(24, 19, NULL);

-- Таблица bank_accounts
DROP TABLE IF EXISTS bank_accounts;
CREATE TABLE bank_accounts (
    bank_account_id INTEGER PRIMARY KEY,
    director_id INTEGER,
    actors_id INTEGER,
    account_number TEXT
);

INSERT INTO bank_accounts (bank_account_id, director_id, actors_id, account_number) VALUES
(1, NULL, 1, '1264567'),
(2, NULL, 2, '1296567'),
(3, NULL, 3, '1234567'),
(4, NULL, 4, '1294167'),
(5, NULL, 5, '1594567'),
(6, NULL, 6, '1794567'),
(7, NULL, 7, '1994567'),
(8, NULL, 8, '2294567'),
(9, NULL, 9, '1294567'),
(10, NULL, 11, '2297667'),
(11, NULL, 11, '3994567'),
(12, NULL, 12, '4294567'),
(13, NULL, 13, '5294567'),
(14, NULL, 14, '6294567'),
(15, 1, NULL, '7294567'),
(16, 2, NULL, '8294567'),
(17, 3, NULL, '9294567'),
(18, 4, NULL, '1294561'),
(19, 5, NULL, '1294562'),
(20, 6, NULL, '1294563'),
(21, 7, NULL, '1294564'),
(22, 8, NULL, '1294565'),
(23, 9, NULL, '1294566'),
(24, 10, NULL, '1294567'),
(25, 11, NULL, '1294568'),
(26, 12, NULL, '1294569'),
(27, 13, NULL, '1294521'),
(28, 14, NULL, '1294537'),
(29, 15, NULL, '1294547'),
(30, 16, NULL, '1294557'),
(31, 17, NULL, '1294557'),
(32, 18, NULL, '1294577');

-- 2.	Добавить новое поле finance INTEGER в таблицу bank_accounts значение задать NULL.

ALTER TABLE bank_accounts ADD COLUMN finance INTEGER DEFAULT NULL;


-- 3.	Вывести первых 10  режиссёров, которые сняли самые высокобюджетные фильмы. Режиссёры не должны повторяться.

SELECT DISTINCT d.director_id, d.name, d.surname, m.budjet
FROM director d
JOIN movies m ON d.director_id = m.director_id
ORDER BY m.budjet DESC
LIMIT 10;


-- 4.	Вывести актёров и режиссёров, которые не участвовали не в одном из фильмов.

-- Актёры без фильмов
SELECT 'actor' AS type, a.actors_id, a.name, a.surname
FROM actors a
LEFT JOIN actors_movies am ON a.actors_id = am.actors_id
WHERE am.actors_movies_id IS NULL

UNION ALL

-- Режиссёры без фильмов
SELECT 'director' AS type, d.director_id, d.name, d.surname
FROM director d
LEFT JOIN movies m ON d.director_id = m.director_id
WHERE m.movie_id IS NULL;


-- 5.	Вывести все фильмы, а также всех актёров кассовые сборы которых превысили 150000000.

SELECT DISTINCT m.movie_id, m.name_movie, m.budjet, a.actors_id, a.name, a.surname
FROM movies m
LEFT JOIN actors_movies am ON m.movie_id = am.movies_id
LEFT JOIN actors a ON am.actors_id = a.actors_id
WHERE m.budjet > 150000000
ORDER BY m.budjet DESC;


-- 6.	Вывести всех режиссёров которые снимали фильмы до 2000 года. Режиссёры не должны повторятся

SELECT DISTINCT d.director_id, d.name, d.surname
FROM director d
JOIN movies m ON d.director_id = m.director_id
WHERE m.release < 2000
ORDER BY d.director_id;


-- 7.	Добавить фильмы для актёров и режиссёров, у которых нет зависимости в таблице movies. Не забыть сделать изменения в таблице actors_movies.

INSERT INTO movies (movie_id, name_movie, release, budjet, director_id) VALUES
(20, 'New Movie for Bruce Willis', 2020, 50000000, 16),
(21, 'New Movie for Halle Berry', 2021, 60000000, 17);

INSERT INTO actors_movies (actors_movies_id, movies_id, actors_id) VALUES
(25, 20, 2),
(26, 21, 11);

INSERT INTO movies (movie_id, name_movie, release, budjet, director_id) VALUES
(22, 'Scorsese New Film', 2022, 80000000, 16),
(23, 'Kubrick Tribute', 2023, 70000000, 17),
(24, 'Allen Project', 2024, 40000000, 18);

INSERT INTO actors_movies (actors_movies_id, movies_id, actors_id) VALUES
(27, 22, NULL),
(28, 23, NULL),
(29, 24, NULL);


-- 8.	Добавить колонку rating к фильмам. Задать значения рейтинга фильмов. 

ALTER TABLE movies ADD COLUMN rating REAL;

-- Значения рейтинга (от 0 до 10)
UPDATE movies SET rating = 8.5 WHERE movie_id = 1;
UPDATE movies SET rating = 7.8 WHERE movie_id = 2;
UPDATE movies SET rating = 9.0 WHERE movie_id = 3;
UPDATE movies SET rating = 8.0 WHERE movie_id = 4;
UPDATE movies SET rating = 7.2 WHERE movie_id = 5;
UPDATE movies SET rating = 8.2 WHERE movie_id = 6;
UPDATE movies SET rating = 7.5 WHERE movie_id = 7;
UPDATE movies SET rating = 6.8 WHERE movie_id = 8;
UPDATE movies SET rating = 7.0 WHERE movie_id = 9;
UPDATE movies SET rating = 7.9 WHERE movie_id = 10;
UPDATE movies SET rating = 6.5 WHERE movie_id = 11;
UPDATE movies SET rating = 8.8 WHERE movie_id = 12;
UPDATE movies SET rating = 8.1 WHERE movie_id = 13;
UPDATE movies SET rating = 5.5 WHERE movie_id = 14;
UPDATE movies SET rating = 7.3 WHERE movie_id = 15;
UPDATE movies SET rating = 6.9 WHERE movie_id = 16;
UPDATE movies SET rating = 7.6 WHERE movie_id = 17;
UPDATE movies SET rating = 8.4 WHERE movie_id = 18;
UPDATE movies SET rating = 8.9 WHERE movie_id = 19;
UPDATE movies SET rating = 7.4 WHERE movie_id = 20;
UPDATE movies SET rating = 7.1 WHERE movie_id = 21;
UPDATE movies SET rating = 8.3 WHERE movie_id = 22;
UPDATE movies SET rating = 8.7 WHERE movie_id = 23;
UPDATE movies SET rating = 6.0 WHERE movie_id = 24;


-- 9.	Вывести режиссёров и фильмы с рейтингом ниже среднего до 2000 года

-- средний рейтинг
WITH avg_rating AS (
    SELECT AVG(rating) AS avg_rate FROM movies WHERE rating IS NOT NULL
)
SELECT d.name, d.surname, m.name_movie, m.release, m.rating
FROM movies m
JOIN director d ON m.director_id = d.director_id
CROSS JOIN avg_rating ar
WHERE m.release < 2000 
  AND m.rating < ar.avg_rate
ORDER BY m.rating ASC;


-- 10.	Вывести всех актёров, которые знакомы с 2-мя и более другими актёрами.

SELECT a.actors_id, a.name, a.surname, COUNT(DISTINCT am2.actors_id) AS known_actors_count
FROM actors a
JOIN actors_movies am1 ON a.actors_id = am1.actors_id
JOIN actors_movies am2 ON am1.movies_id = am2.movies_id AND am1.actors_id != am2.actors_id
WHERE am2.actors_id IS NOT NULL
GROUP BY a.actors_id, a.name, a.surname
HAVING COUNT(DISTINCT am2.actors_id) >= 2
ORDER BY known_actors_count DESC;