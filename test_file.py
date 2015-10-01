import csv


def open_csv(filename):
    with open(filename, 'r') as f:
        data = csv.reader(f)
        return list(data)

filename = "gutenbergscifi.csv"

data = open_csv(filename)

print data