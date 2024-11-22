# python program to write contents into a csv file using DictWriter object of csv module

import csv

covid_data = [{'Country': 'India', 'Doses': '186Cr' , 'People': '84.1Cr', 'Percentage':61}, 
{'Country': 'China', 'Doses': '330Cr', 'People': '124Cr', 'Percentage':88.1},
{'Country': 'United States', 'Doses':'56.8Cr', 'People': '21.9Cr', 'Percentage':66.4},
{'Country': 'Brazil', 'Doses': '42.4Cr', 'People': '16.2Cr', 'Percentage':76.4},
{'Country': 'Indonesia', 'Doses': '39Cr', 'People': '16.2Cr', 'Percentage':59.3}]

# opening a csv file in write mode
f = open('D:\\Learn-Github-Repositories\\Learn Python Programming - Beginner to Master\\23.OS Module\\Writing CSV File using DictWriter\\Covid_data.csv', 'w', newline='')

fields = ['Country', 'Doses', 'People', 'Percentage']

# creating a DictWriter object
dwr = csv.DictWriter(f, fieldnames=fields)

dwr.writeheader()   # writing the column names in the first row of the csv file (Covid_data)

for row in covid_data:
    dwr.writerow(row)

# closing the csv file
f.close()