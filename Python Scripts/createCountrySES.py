
# this script was written to create the .csv file with all countries and their socio-economical status (SES)


import pandas as pd

count = pd.read_csv("CountFinal.csv")
allDB = pd.read_csv("summer.csv")


def olympicrange(start, end, step):
    while start <= end:
        yield start
        start += step


for column in count:
    if column == 'Country':
        listAll = (list(count[column]))

listYears = []

for x in olympicrange(1948,2012,4):
    listYears.append(x)

for column in count:
    if column == 'Country':
        listAll = (list(count[column]))


listDictionary = dict((year, dict((country, 0) for country in listAll)) for year in listYears)


for index, row in allDB.iterrows():
            listDictionary[row['Year']][row['Country']] += 1


with open('ssemedals.csv', 'w') as f:
    f.write("%s,%s,%s, %s\n" % ('Country', 'Year', 'Developed','Medals'))
    for country in listAll:
        for year in listYears:
            f.write("%s,%s,%s, %s\n" % (country, year, 'F', listDictionary[year][country]))
