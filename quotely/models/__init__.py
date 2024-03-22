import sqlite3

CONN = sqlite3.connect('quotes.db')
CURSOR = CONN.cursor()
