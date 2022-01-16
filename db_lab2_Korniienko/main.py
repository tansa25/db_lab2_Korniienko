import psycopg2

username = 'postgres'
password = '25012002'
database = 'lab2_database'
host = 'localhost'
port = '5432'


query_1 = '''
SELECT genre_name AS genre, 
COUNT(genre_id) FROM Books 
JOIN Genre USING(genre_id) 
GROUP BY genre_name
'''

query_2 = '''
SELECT author.author_name, count(author.author_name) 
FROM Books INNER JOIN author ON Books.author_id = author.author_id
GROUP BY author.author_name
'''

query_3 = '''
SELECT period.period_year, count(period.period_year) 
FROM Books INNER JOIN period ON Books.period_id = period.period_id
GROUP BY period.period_year
'''

con = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)


with con:

    cur = con.cursor()

    print('query 1:\n')
    cur.execute(query_1)
    for row in cur:
      print(row)

    print('\n\nquery 2:\n')
    cur.execute(query_2)
    for row in cur:
      print(row)

    print('\n\nquery 3:\n')
    cur.execute(query_3)
    for row in cur:
      print(row)
