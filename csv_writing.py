import csv

with open('newcsv.csv', 'w') as file:
    writer = csv.DictWriter(file, ['name', 'email'])
    writer.writeheader()
    writer.writerow({'name':'Bikalpa', 'email':'abc@xyz.com'})