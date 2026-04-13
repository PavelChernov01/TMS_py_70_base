DROP TABLE IF EXISTS actors;

CREATE TABLE actors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    age INTEGER,
    sex TEXT CHECK (sex IN ('male', 'female')),
    country TEXT,
    name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

ALTER TABLE actors ADD COLUMN salary INTEGER;

DROP TABLE IF EXISTS actors_old;
CREATE TABLE actors_old AS SELECT * FROM actors;

DROP TABLE actors;

CREATE TABLE actors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    age INTEGER CHECK (age >= 0),
    sex TEXT CHECK (sex IN ('male', 'female')),
    country TEXT,
    name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    salary INTEGER
);
INSERT INTO actors (id, age, sex, country, name, last_name, salary)
SELECT id, age, sex, country, name, last_name, salary FROM actors_old;

DROP TABLE actors_old;

CREATE TABLE actors_new (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    age INTEGER CHECK (age >= 0),
    sex TEXT CHECK (sex IN ('male', 'female')),
    country TEXT,
    name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

INSERT INTO actors_new (id, age, sex, country, name, last_name)
SELECT id, age, sex, country, name, last_name FROM actors;

DROP TABLE actors;
ALTER TABLE actors_new RENAME TO actors;

INSERT INTO actors (age, sex, country, name, last_name) VALUES
(78, 'male', 'USA', 'Arnold', 'Schwarzenegger'),
(70, 'male', 'USA', 'Bruce', 'Willis'),
(63, 'male', 'USA', 'Tom', 'Cruise'),
(62, 'male', 'USA', 'Brad', 'Pitt'),
(57, 'male', 'USA', 'Will', 'Smith'),
(51, 'male', 'USA', 'Leonardo', 'DiCaprio'),
(69, 'male', 'USA', 'Tom', 'Hanks'),
(62, 'male', 'USA', 'Johnny', 'Depp'),
(83, 'male', 'USA', 'Harrison', 'Ford'),
(61, 'female', 'USA', 'Sandra', 'Bullock'),
(59, 'female', 'USA', 'Halle', 'Berry'),
(58, 'female', 'USA', 'Julia', 'Roberts'),
(50, 'female', 'UK', 'Kate', 'Winslet'),
(50, 'female', 'USA', 'Angelina', 'Jolie'),
(71, 'male', 'China', 'Jackie', 'Chan'),
(51, 'female', 'Spain', 'Penélope', 'Cruz'),
(53, 'male', 'UK', 'Idris', 'Elba'),
(42, 'female', 'Kenya', 'Lupita', 'Nyong''o'),
(60, 'male', 'Denmark', 'Mads', 'Mikkelsen'),
(50, 'female', 'France', 'Marion', 'Cotillard'),
(35, 'male', 'UK', 'Dev', 'Patel'),
(70, 'male', 'USA', 'Willem', 'Dafoe'),
(68, 'male', 'Argentina', 'Ricardo', 'Darin'),
(39, 'female', 'India', 'Deepika', 'Padukone'),
(63, 'male', 'China', 'Tony', 'Leung'),
(46, 'female', 'Sweden', 'Noomi', 'Rapace'),
(47, 'male', 'Germany', 'Daniel', 'Brühl'),
(42, 'female', 'Iran', 'Golshifteh', 'Farahani'),
(57, 'male', 'Australia', 'Hugh', 'Jackman'),
(72, 'female', 'France', 'Isabelle', 'Huppert');

INSERT INTO actors (name, last_name) VALUES
('James', 'McAvoy'),
('Emma', 'Stone'),
('Joaquin', 'Phoenix'),
('Cate', 'Blanchett'),
('Matthew', 'McConaughey');

UPDATE actors 
SET country = 'Unknown' 
WHERE country IS NULL;

UPDATE actors 
SET age = age + 2 
WHERE sex = 'female' AND age > 40;

SELECT * FROM actors 
WHERE sex = 'female' 
  AND country = 'France' 
  AND age < 35;

SELECT * FROM actors 
ORDER BY age ASC 
LIMIT 5;

SELECT 
    COUNT(*) AS total_actors,
    AVG(age) AS average_age,
    MIN(age) AS min_age,
    MAX(age) AS max_age
FROM actors
WHERE age IS NOT NULL;

SELECT country, COUNT(*) AS actors_count
FROM actors
GROUP BY country
HAVING COUNT(*) > 5 AND COUNT(*) < 10
ORDER BY actors_count DESC;  

SELECT 
    sex,
    ROUND(AVG(age), 1) AS average_age
FROM actors
WHERE age IS NOT NULL
GROUP BY sex;

SELECT 
    country,
    name,
    last_name,
    age,
    sex
FROM actors a1
WHERE age IS NOT NULL
  AND age = (
    SELECT MIN(age)
    FROM actors a2
    WHERE a2.country = a1.country
      AND a2.age IS NOT NULL
  )
ORDER BY country;

SELECT country
FROM actors
GROUP BY country
HAVING SUM(CASE WHEN sex = 'female' THEN 1 ELSE 0 END) = 0;