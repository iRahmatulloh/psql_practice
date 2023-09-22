import psycopg2

DB = "transaction"
USER = "postgres"
HOST = 'localhost'
PORT = 5432
PASSWORD = "0571"

connection = psycopg2.connect(database=DB, user=USER, host=HOST, port=PORT, password=PASSWORD)
cur = connection.cursor()
