import csv

with open('DIN_Values_Test1md
') as csvfile:
    readCSV = csv.reader(csvfile, delimiter='\n')
    for row in readCSV:
        print(row)
        print(row[0])
        print(row[0],row[1],row[2],)