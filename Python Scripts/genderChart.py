
# this script was written to create the .csv file with the information for the gender comparison graph

import pandas as pd


allDB = pd.read_csv("summer.csv")
count = pd.read_csv("CountFinal.csv")


# these are the countries we wish to examine


countries = ['United States of America', 'Australia', 'Canada', 'Croatia', 'Pakistan', 'India']

menDictionary = dict((country, 0) for country in countries)

womenDictionary = dict((country, 0) for country in countries)

for index, row in allDB.iterrows():
    if row['Country'] in countries:
        if row['Gender'] == 'Women':
            womenDictionary[row['Country']] += 1
        else:
            menDictionary[row['Country']] += 1

with open('test.csv', 'w') as f:
    f.write("%s,%s\n" % ('Country', 'Medals'))
    for country in countries:
            f.write("%s,%s\n" % (country+" Men", menDictionary[country]))
            f.write("%s,%s\n" % (country+" Women", womenDictionary[country]))