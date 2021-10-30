import csv
path = 'D:\memor\Documents\Programming\Python\Projetos\Anki_Vocabulary\eggs.csv'
pathNames = r'D:\memor\Documents\Programming\Python\Projetos\Anki_Vocabulary\names.csv'

# with open(path, 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

# with open(path, newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))

# with open(pathNames, 'w', newline='') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

# with open(pathNames, newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row['first_name'], row['last_name'])

# csv.QUOTE_ALL
# QUOTE_MINIMAL
# QUOTE_NONNUMERIC
# QUOTE_NONE


# ===============================================================
# THE SIMPLES POSSIBLES EXAMPLES
# ===============================================================

# with open('some.csv', newline='') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# with open('some.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerows(someiterable)

# # FILE WITH DIFFERENT ENCODING
# with open('some.csv', newline='', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)