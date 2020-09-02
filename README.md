# cvrapi-cvrcsv2datacsv

## What this does

This python3 script reads one column of cvr (VAT) codes from a headerless csv file.
Each entry is sent to the cvrapi.dk and returns a json array with company data.
The number of employees is extracted from the resultset and saved as a new row into a new csv file.


## What you need

Read the documentation in the link below

* python3
* 1 csv file with danish cvr / vat numbers

Only request 50 values pr. run on the free api account


## Run the script
Run the script like 

python3 main.py 

or run it from your preferred IDE.



### Links to the API and documentation

[CVRAPI.dk Documentation](https://cvrapi.dk/documentation)


### Ideas and suggestions
Let me know.

### USAGE DISCLAIMER

READ THE DOCUMENTATION and adhere to it.
