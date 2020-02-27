import csv
with open('users.csv', 'r', encoding='utf-8') as my_file:
    fields = ['first_name', 'last_name', 'email', 'gender', 'balance']
    reader = csv.DictReader(my_file, fields, delimiter=';')
    money_total = 0
    for row in reader:
        print(dict(row))
        money_total += float(row['balance'])
    print(money_total)

user_list = [
    {'first_name': 'Gloria', 'last_name': 'Armstrong', 'email': 'garmstrong0@harvard.edu', 'gender': 'Female', 'balance': '8.82'},
    {'first_name': 'Amanda', 'last_name': 'Scott', 'email': 'ascott1@skyrock.com', 'gender': 'Female', 'balance': '9.5'},
    {'first_name': 'Glohria', 'last_name': 'Armfstrong', 'email': 'garmsttghrong0@harvard.edu', 'gender': 'Female', 'balance': '8.82'},
    {'first_name': 'Amhanda', 'last_name': 'Scoftt', 'email': 'asgcott1@sgkyrock.com', 'gender': 'Female', 'balance': '99.5'}
    ]

with open('export.csv', 'w', encoding='utf-8', newline='') as my_file:
    fields = ['first_name', 'last_name', 'email', 'gender', 'balance']
    writer = csv.DictWriter(my_file, fields, delimiter=';')
    writer.writeheader()
    for user in user_list:
        writer.writerow(user)