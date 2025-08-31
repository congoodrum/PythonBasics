import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

try:
    with open('packing_list.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("packing_list.csv is not found. Creating a new file...")
    
    with open('packing_list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    # with open('output.csv', 'w', newline='') as file:
    #     output = csv.writer(file)
    #     output.writerows([headers, best_seller])