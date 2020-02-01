########################################
# Program: This program reads google sheet and writes to a CSV file
# Author: Neil Deo
# Input: None - URL of the spreadsheet is hardcoded
# Output: CSV file - put.csv in the same directory
########################################
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv
from math import cos, asin,sqrt
import time
start_time = time.time()
# Let's define all the constants - that can be configured easily
fileForCreds = 'ex.json'
googleSheetName =  'Final Basic Info (Responses)'
outputFileName = 'put.csv'
userCountry = []
continent = []
checkCountry = []
indexes = []
userContinents = []
# Craete scope for google drive and read credentials from ex.json
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(fileForCreds, scope)
# Authorize the credentials and open teh spreadsheet
client = gspread.authorize(creds)
sheet = client.open(googleSheetName).sheet1
## get all values - returns the entire data in the spreadsheet as list of rows
responses = sheet.get_all_values()
with open (outputFileName,'w',newline='') as f:
    writer = csv.writer(f)
    for i in responses:
        # write one response row at a time converting it to a List as [i]'
        writer.writerows([i])
with open(outputFileName,'r',newline = '') as f:
    reader = csv.reader(f, delimiter = ',')
    for i in reader:
        userCountry.append(i[6])
userCountry.pop(0)
with open ('countries.csv','r',newline = '') as r:
    reader = csv.reader(r,delimiter = ',')
    for i in reader:
        continent.append(i[0])
        checkCountry.append(i[2])
continent.pop(0)
checkCountry.pop(0)
for i,c in enumerate(userCountry):
    for j in range(len(checkCountry)):
        if c in checkCountry[j]:
            indexes.append(j)

for i in range(len(indexes)):
    print(checkCountry[indexes[i]],continent[indexes[i]])
    userContinents.append(continent[indexes[i]])

print(indexes)
print(len(userContinents),len(userCountry))
print(userContinents)
print('#################################')
print(userCountry)
print(time.time()-start_time)
