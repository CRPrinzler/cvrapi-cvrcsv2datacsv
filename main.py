@author: CRPrinzler
"""

import urllib.request as request
import json 
import csv 
from csv import reader
import contextlib
import time


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
    url='http://cvrapi.dk/api?search=' + cvr + '&country=%s' % (country),
    headers={
      'User-Agent': 'INSERT YOUR AGENT DATA HERE adhere to documentation'})
    with contextlib.closing(request.urlopen(request_a)) as response:
     #get employee data
     y = (json.loads(response.read()))
     #save the data to csv
     csvRow = [y["employees"]]
     print(csvRow)
     csvfile = "data.csv"
     with open(csvfile, "a") as fp:
      wr = csv.writer(fp, dialect='excel')
      wr.writerow(csvRow)
      #Go to sleep for some seconds in order not to stress the API
      time.sleep(60)
  else:
      print("DONE")
