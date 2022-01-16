-- query 1 --
--number of books of each genre--

SELECT genre_name AS genre, 
COUNT(genre_id) FROM Books 
JOIN Genre USING(genre_id) GROUP BY genre_name

-- query 2 --
--number of books by each author--

SELECT author.author_name, COUNT(author.author_name) 
FROM Books INNER JOIN author ON Books.author_id = author.author_id
GROUP BY author.author_name

-- query 3 --
--number of books each year--

SELECT period.period_year, COUNT(period.period_year) 
FROM Books INNER JOIN period ON Books.period_id = period.period_id
GROUP BY period.period_year