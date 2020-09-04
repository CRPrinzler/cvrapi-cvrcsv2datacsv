@author: CRPrinzler
"""

import urllib.request as request
import urllib.error
import json 
import csv 
from csv import reader
import contextlib
#import time


#Remember to read the cvrapi.dk documentation and adhere to the usage terms.



#Setting the country for the api  
country='dk'  



# open file in read mode
with open('cvr.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
  csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
  for row in csv_reader:
        # row variable is a list that represents a row in csv
    cvr = row[0]
    #uncomment next line if you want to see whats going on.
    #print(cvr)
    #call API
    request_a = request.Request(
    url='https://cvrapi.dk/api?search='+cvr+'&country=%s' % (country),
    headers={
    'User-Agent': 'YOUR AGENT DATA GOES HERE})
        
    try:
        with contextlib.closing(request.urlopen(request_a)) as response:
            y = (json.loads(response.read()))   
    except urllib.error.HTTPError as e:
        print('HTTPError: {}'.format(e.code))
    
    else:
     #get employee data
     try:
         csvRow = [y["employees"]]
         #save the data to csv
         print(csvRow)
         csvfile = "datapull.csv"
         with open(csvfile, "a") as fp:
          wr = csv.writer(fp, dialect='excel')
          wr.writerow(csvRow)
      
     except KeyError:
         csvRow = "NOT_FOUND"
         #save the data to csv
         #print(csvRow)
         csvfile = "datapull.csv"
         with open(csvfile, "a") as fp:
          wr = csv.writer(fp, dialect='excel')
          wr.writerow(csvRow)
         
  else:
      print("DONE")

