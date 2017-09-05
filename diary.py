import csv


class Diary():

    def __init__(self):
        self.file = "data.csv"

    def file_read(self):
        with open('%s' % self.file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row['date'], row['description'])

    def file_safe(self, custom_date, description):
        with open('%s' % self.file, 'a') as csvfile:
            filewriter = csv.writer(csvfile)
            filewriter.writerow([custom_date, description])