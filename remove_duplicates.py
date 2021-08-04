import csv

path = 'D:\memor\Documents\Programming\Python\Projetos\Anki_Vocabulary\English_Words.csv'
newrows = []
with open(path, 'r', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if row not in newrows:
            newrows.append(row)

with open(path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(newrows)