#task2
import sqlite3

conn = sqlite3.connect("internship.db")

query = """
SELECT 
    i.name AS intern_name,
    i.track,
    i.stipend,
    m.mentor_name
FROM interns i
INNER JOIN mentors m
ON i.track = m.track;
"""

df = pd.read_sql_query(query, conn)
df

df.head()
df.describe()
df.groupby("track")["stipend"].mean()