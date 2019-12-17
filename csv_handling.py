import csv

with open('student.csv') as file:
    rows = csv.DictReader(file)
    for row in rows:
        print(row['email'])