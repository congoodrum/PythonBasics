import csv

# file = open('Intermediate Course\Exercises\2 - File I_O\Bestseller - Sheet1.csv', 'r')

with open('Bestseller - Sheet1.csv', 'r', encoding='utf8') as file:
    headers = None
    best_seller = None
    row_count = 0
    csv_reader = csv.reader(file)

    for row in csv_reader:
        if row_count == 0:
           headers = row
           row_count += 1
           continue
        if best_seller == None or float(best_seller[4]) < float(row[4]):
            best_seller = row

    with open('output.csv', 'w', newline='') as file:
        output = csv.writer(file)
        output.writerows([headers, best_seller])