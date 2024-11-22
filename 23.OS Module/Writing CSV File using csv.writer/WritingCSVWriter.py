# python program to write data from python into csv file using csv module's builtin class writer

import csv 

# covid data
covid_data = [('Country', 'Doses', 'People', 'Percentage'),
('India', '186Cr', '84.1Cr', 61),
('China', '330Cr', '124Cr', 88.1),
('United States', '56.8Cr', '21.9Cr', 66.4),
('Brazil', '42.4Cr', '16.2Cr', 76.4),
('Indonesia', '39Cr', '16.2Cr', 59.3)]

# opening a csv file
f = open('D:\\Learn-Github-Repositories\\Learn Python Programming - Beginner to Master\\23.OS Module\\Writing CSV File using csv.writer', 'w', newline='')

# creating an object for writer class
wr = csv.writer(f)

for row in covid_data:
    wr.writerow(row)
    
# closing the csv file
f.close()