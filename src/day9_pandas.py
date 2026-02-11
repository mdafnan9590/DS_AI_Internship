
#task1
import pandas as pd
values= pd.Series([ 700, 150, 300], index = ('Laptop', 'Mouse', 'Keyboard'))
print(values)
print(values[['Laptop']])
print(values[0:2])


#task2
data =pd.Series([85, None, 92, 45, None, 78, 55])
print(data.isnull())
print(data.fillna(0))

greater_than_60 = data[data>60]
print(data)


#TASK 3

usernames = pd.Series(['Alice', 'boB', 'Charlie_Data', 'daisy'])
print(usernames)
strip = usernames.str.strip()
print(strip)
lower = usernames.str.lower()
print(lower)
print(usernames.str.contains('a'))

print(strip)
print(lower)
print(usernames.str.contains('a'))


