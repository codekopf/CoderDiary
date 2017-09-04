import csv

def read_file():
    with open('data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['date'], row['description'])

if __name__ == '__main__':
    read_file()
