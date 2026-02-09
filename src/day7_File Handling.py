#ask1
name=input("enter your name:")
goal=input("enteryour daily goal:")

with open("journal.txt","a") as file: 
    file.write(f"{name}-{goal}\n")

with open("journal.txt","r") as file:
    a=file.read()
    print(a)
    
    
#task 2

import csv

with open("student.csv","r") as file:
    reader=csv.DictReader(file)

    print("students who has passedi")

    for row in reader:
        if row ["Status"]=="Pass":
            print(row["Name"])    


#task3

filename = input("Enter a filename ")

try:
    with open(filename, "r") as file:
        contents = file.read()
        print("File contents:")
        print(contents)

except FileNotFoundError:
    print("Oops! That file doesn't exist yet.")