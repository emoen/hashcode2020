import csv
       
csv_row = list()       
for line in open("a_example.txt"):
    csv_row.append( line.split())

B = csv_row[0][0] #books
L = csv_row[0][1] #libraries
S = csv_row[0][2] #days for scanning

