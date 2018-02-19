#Your task is to create a Python script that analyzes the records to calculate each of the following:

#The total number of months included in the dataset

#The total amount of revenue gained over the entire period

#The average change in revenue between months over the entire period

#The greatest increase in revenue (date and amount) over the entire period

#The greatest decrease in revenue (date and amount) over the entire period

#As an example, your analysis should look similar to the one below:

# =============================================================================
# Financial Analysis
# ----------------------------
# Total Months: 25
# Total Revenue: $1241412
# Average Revenue Change: $216825
# Greatest Increase in Revenue: Sep-16 ($815531)
# Greatest Decrease in Revenue: Aug-12 ($-652794)
# =============================================================================




# First we'll import the os module 
# This will allow us to create file paths across operating systems
import os

#list of data files that you can add more to if required
fileList = ["budget_data_1.csv","budget_data_2.csv"]


for file in fileList:
    #reset all the values
    totalMonths = 0
    totalRevenue = 0
    avgRevenueChange = 0
    greatestRevIncDate = ""
    greatestRevIncAmt = 0
    greatestRevDecDate = ""
    greatestRevDecAmt = 0
    totalRevenueChange = 0
    prevRevenue = 0
    revIncrease = 0
    #assumes data files exist in the directory raw_data which is at the same level
    #as the script
    csvpath = os.path.join("raw_data",file)
    #print(csvpath)
    import csv
    with open(csvpath, newline='') as csvfile:
        
        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
        #skip the header row
        next(csvreader)
        
        

        #  Each row is read as a row
        for row in csvreader:
            #print(row)
            totalRevenue = totalRevenue + int(row[1])
            totalMonths = totalMonths +1
            #skip the first month for revenue change
            if totalMonths > 1:
                revIncrease = int(row[1]) - prevRevenue
                totalRevenueChange = totalRevenueChange + revIncrease
            prevRevenue =  int(row[1])
            if(revIncrease > greatestRevIncAmt):
                greatestRevIncAmt = revIncrease
                greatestRevIncDate = row[0]
            
            if(revIncrease < greatestRevDecAmt):
                greatestRevDecAmt = revIncrease
                greatestRevDecDate = row[0]

    #When calculating the average revenue change the intervals is one less than total months
    avgRevenueChange = round(totalRevenueChange/(totalMonths-1),2)

   #create and open output file to write resuts to
    outputpath = os.path.join("raw_data",file.split(".")[0] + "_Results.txt")

    lines = []
    
    resultsfile = open(outputpath, "w")
    
    #create the output
    lines.append("Financial Analysis")
    lines.append("----------------------------")
    lines.append("Total Months: "+str(totalMonths))
    lines.append("Total Revenue: $" + str(totalRevenue))
    lines.append("Average Revenue Change: $"+str(avgRevenueChange))
    lines.append("Greatest Increase in Revenue: "+greatestRevIncDate + " ($" + str(greatestRevIncAmt) +")")
    lines.append("Greatest Decrease in Revenue: "+greatestRevDecDate + " ($" + str(greatestRevDecAmt) +")")

     ##Write the output to file and console
    for line in lines:
        print(line)
        print(line,file=resultsfile)
        
    #new line
    print()
    
    #close the file
    resultsfile.close()