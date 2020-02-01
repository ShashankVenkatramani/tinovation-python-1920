########################################
# Program: This program reads google sheet and writes to a CSV file
# Author: Neil Deo
# Input: None - URL of the spreadsheet is hardcoded
# Output: CSV file - put.csv in the same directory
########################################
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv
from geopy.geocoders import Nominatim
from math import cos, asin,sqrt
import time
start_time = time.time()
def findDistance(latOne,latTwo,lonOne,lonTwo):
   p = 0.017453292519943295
   a = 0.5 - cos((latTwo - latOne) * p)/2 + cos(latOne * p) * cos(latTwo * p) * (1 - cos((lonTwo - lonOne) * p)) / 2
   distance = 12742 * asin(sqrt(a))
   return distance
try:
   # Let's define all the constants - that can be configured easily
   fileForCreds = 'ex.json'
   googleSheetName =  'Final Basic Info (Responses)'
   outputFileName = 'put.csv'
   country = []
   lat = []
   lon = []
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
         country.append(i[6])
   country.pop(0)
   print(time.time()-start_time)
   for i in country:
      try:
         geolocator = Nominatim(user_agent = 'tinovation-project')
         location = geolocator.geocode(i)

         print(i,location.latitude,location.longitude)
         lat.append(abs(location.latitude))
         lon.append(abs(location.longitude))
      except Exception as e:
         print("Invalid Country Exception")
         print(str(e))
   print(time.time()-start_time)
   bigArr = []
   for i in range(len(country)):
      for j in range(len(country)):
         maxDist = findDistance(lat[i],lat[j],lon[i],lon[j])
         bigArr.append([country[i],country[j],maxDist])


   for i in bigArr:
      print(i[0],i[1],i[2])
except Exception as e:
   print(str(e))






























