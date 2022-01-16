import psycopg2
import matplotlib.pyplot as plt

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

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()

    cur.execute(query_1)
    data_to_visualise = {}

    for row in cur:
      data_to_visualise[row[0]] = row[1]

    x_range = range(len(data_to_visualise.keys()))
 
    figure, bar_ax = plt.subplots()
    bar = bar_ax.bar(x_range, data_to_visualise.values(), label='Total')
    bar_ax.set_title('number of books of each genre')
    bar_ax.set_xlabel('Genre')
    bar_ax.set_ylabel('Amount')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(data_to_visualise.keys())


    cur.execute(query_2)
    data_to_visualise = {}

    for row in cur:
      data_to_visualise[row[0]] = row[1]

    figure, pie_ax = plt.subplots()
    pie_ax.pie(data_to_visualise.values(), labels=data_to_visualise.keys(), autopct='%1.1f%%')
    pie_ax.set_title('number of books by each author')


    cur.execute(query_3)
    data_to_visualise = {}

    for row in cur:
      data_to_visualise[row[0]] = row[1]

    x_range = range(len(data_to_visualise.keys()))
 
    figure, bar_ax = plt.subplots()
    bar = bar_ax.bar(x_range, data_to_visualise.values(), label='Total')
    bar_ax.set_title('number of books each year')
    bar_ax.set_xlabel("Year")
    bar_ax.set_ylabel('Amount')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(data_to_visualise.keys())


mng = plt.get_current_fig_manager()
mng.resize(1000, 500)

plt.show()
