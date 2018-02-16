# Your task is to help bridge the gap by creating a Python script able to convert your employee records 
# to the required format. Your script will need to do the following:

# Import the employee_data1.csv and employee_data2.csv files, which currently holds employee records 
# like the below:
# Emp ID,Name,DOB,SSN,State
# 214,Sarah Simpson,1985-12-04,282-01-8166,Florida
# 15,Samantha Lara,1993-09-08,848-80-7526,Colorado
# 411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
# Then convert and export the data to use the following format instead:
# Emp ID,First Name,Last Name,DOB,SSN,State
# 214,Sarah,Simpson,12/04/1985,***-**-8166,FL
# 15,Samantha,Lara,09/08/1993,***-**-7526,CO
# 411,Stacy,Charles,12/20/1957,***-**-8526,PA
# In summary, the required conversions are as follows:

# The Name column should be split into separate First Name and Last Name columns.

# The DOB data should be re-written into DD/MM/YYYY format.

# The SSN data should be re-written such that the first five numbers are hidden from view.

# The State data should be re-written as simple two-letter abbreviations.

# First we'll import the os module 
# This will allow us to create file paths across operating systems

##Dictionary for state abbreviations
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

import os

#List of data files. Append any other data files as required
dataFileList = ["employee_data1.csv","employee_data2.csv"]

for file in dataFileList:
    #assumes data files exist in the directory raw_data which is at the same level
    #as the script
    csvpath = os.path.join("raw_data",file)
    
    #output file with formatted data
    formattedCsvpath = os.path.join("raw_data","formatted_"+file)


    
    import csv
    #open the formatted csv file to write in 
    with open(formattedCsvpath,'w',newline='') as formattedCsvfile:
        csvwriter = csv.writer(formattedCsvfile)
        #write the header row
        csvwriter.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])
        with open(csvpath, newline='') as csvfile:
            #skip the header row
            csvfile.readline()

            # CSV reader specifies delimiter and variable that holds contents
            csvreader = csv.reader(csvfile, delimiter=',')

            #  Each row is read as a row
            for row in csvreader:
                empID = row[0]
                empName = row[1]
                empDOB = row[2]
                empSSN = row[3]
                empState = row[4]

                #do the necessary formatting and write each formatted row to new file
                splitName = empName.split()
                empFirstName = splitName[0]
                empLastName = splitName[1]

                splitDOB =  empDOB.split("-")
                dobYear = splitDOB[0]
                dobMonth = splitDOB[1]
                dobDay = splitDOB[2]
                formattedDOB = dobMonth + "/" + dobDay + "/" + dobYear

                formattedSSN = "***-**-" + empSSN.split("-")[2]

                abbrState = us_state_abbrev.get(empState)

                #write each row to the formatted file
                csvwriter.writerow([empID,empFirstName,empLastName,formattedDOB,formattedSSN,abbrState])
                #print(str([empID,empFirstName,empLastName,formattedDOB,formattedSSN,abbrState]))
    formattedCsvfile.close()