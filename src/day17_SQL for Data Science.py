#topic 
import pandas as pd

import sqlite3

conn = sqlite3.connect("C:/Users/MD AFNAN/Desktop/database/demo3.db")

df = pd.read_sql_query("SELECT * FROM students",conn)

print(df)


#task1

import pandas as pd

import sqlite3

conn = sqlite3.connect("C:/Users/MD AFNAN/Desktop/database/internship.db")

df = pd.read_sql_query("SELECT name, track FROM interns",conn)
print(df)

