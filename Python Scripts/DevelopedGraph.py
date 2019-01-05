
# this script was written to create the .csv file with the appropriate information for the
# "Developed VS Developing" graph

import pandas as pd


allDB = pd.read_csv("summer.csv")
Developed = pd.read_csv("SESFinal.csv")
count = pd.read_csv("CountFinal.csv")


def olympicrange(start, end, step):
    while start <= end:
        yield start
        start += step


listYears = []

for x in olympicrange(1948,2012,4):
    listYears.append(x)


developingDictionary = dict((year, 0) for year in listYears)
for index, row in Developed.iterrows():
    if row['Developed'] == 'F':
        developingDictionary[row['Year']] += row['Medals']

developedDictionary = dict((year, 0) for year in listYears)
for index, row in Developed.iterrows():
    if row['Developed'] == 'T':
        developedDictionary[row['Year']] += row['Medals']

with open('devgraph.csv', 'w') as f:
    f.write("%s,%s, %s, %s\n" % ('Year', 'Total', 'Developing', 'Developed'))
    for year in listYears:
        f.write("%s,%s, %s, %s\n"%(year, developingDictionary[year]+developedDictionary[year], developingDictionary[year], developedDictionary[year]))




