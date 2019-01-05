# this script was written to create the .csv file with all countries and amount of medals they won in every specific year


import pandas as pd
import collections

def olympicrange(start, end, step):
    while start <= end:
        yield start
        start += step


count = pd.read_csv("countMedalsFinal.csv")
allDB = pd.read_csv("allDB.csv")

for column in count:
    if column == 'Country':
        listAll = (list(count[column]))


listYears = []

for x in olympicrange(1948,2012,4):
    listYears.append(x)


listDictionary = dict((year, dict((country, 0) for country in listAll)) for year in listYears)


for index, row in allDB.iterrows():
    listDictionary[row['Year']][row['Country']] += 1


with open('medalsByYears.csv', 'w') as f:
    f.write("%s,%s,%s\n" % ('Year', 'Country', 'Count'))
    for year in listYears:
        for country in listDictionary[year].keys():
            f.write("%s,%s,%s\n"%(year,country,listDictionary[year][country]))

