import csv

with open('student.csv') as old_file:
    with open('newcsv.csv', 'w') as new_file:
        reader = csv.DictReader(old_file)
        writer = csv.DictWriter(new_file, ['name', 'email'])
        writer.writeheader()

        for row in reader:
            if int(row['sn']) % 2 == 0:
                d = {
                    'name': row['name'],
                    'email': row['email']
                }
                writer.writerow(d) 