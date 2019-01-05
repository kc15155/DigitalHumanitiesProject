
# this script was written to create the .csv file with all countries and amount of medals they won


import pandas as pd
import collections


allDB = pd.read_csv("summer.csv")

for column in allDB:
    if column == 'Country':
        listAll = (list(allDB[column]))

listAll = (set(listAll))

listDictionary = dict((x, 0) for x in listAll)
listDictionary = collections.OrderedDict(sorted(listDictionary.items()))

for index, row in allDB.iterrows():
        listDictionary[row['Country']] += 1

with open('countMedalsFinal.csv', 'w') as f:
    f.write("%s,%s\n" % ('Country', 'Count'))
    for key in listDictionary.keys():
        f.write("%s,%s\n"%(key,listDictionary[key]))

