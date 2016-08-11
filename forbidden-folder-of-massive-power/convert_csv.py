import sys
import csv
import json

csvfile = open('hillary.csv', 'r')
jsonfile = open('test.json', 'w')  

reader = csv.DictReader(csvfile)  

for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')

jsonfile.close()
csvfile.close()
