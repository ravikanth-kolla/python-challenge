# You will be given two sets of poll data (election_data_1.csv and election_data_2.csv). 
# Each dataset is composed of three columns: Voter ID, County, and Candidate. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:

# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

# As an example, your analysis should look similar to the one below:

# Election Results
# -------------------------
# Total Votes: 620100
# -------------------------
# Rogers: 36.0% (223236)
# Gomez: 54.0% (334854)
# Brentwood: 4.0% (24804)
# Higgins: 6.0% (37206)
# -------------------------
# Winner: Gomez
# -------------------------
# Your final script must be able to handle any such similarly-structured dataset in the future 
# (i.e you have zero intentions of living in this hillbilly town -- so your script needs to work 
# without massive re-writes). In addition, your final script should both print the analysis to 
# the terminal and export a text file with the results.



# First we'll import the os module 
# This will allow us to create file paths across operating systems
import os

#List of data files. Append any other data files as required
dataFileList = ["election_data_1.csv","election_data_2.csv"]

for file in dataFileList:
    # assumes data files exist in the directory raw_data which is at the same
    # level as the script
    csvpath = os.path.join("raw_data", file)
    print(csvpath)
    import csv
    with open(csvpath, newline='') as csvfile:
        

        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
        #Reset values
        totalVotes = 0
        candidateList = []
        voteCountList = []
        
        #skip the header row
        next(csvreader)
        #  Each row is read as a row
        for row in csvreader:
            
            #increment total votes
            totalVotes = totalVotes+1
            candidate = row[2]
            #check if first vote for this candidate has been counted
            if not candidate in candidateList:
               candidateList.append(candidate)
               #add first vote for this candidate
               voteCountList.append(1)
            #else add another vote for this candidate
            else:
                indexofCandidate =  candidateList.index(candidate)
                curVoteTally = voteCountList[indexofCandidate]
                #increase vote tally for this candidate by 1
                voteCountList[indexofCandidate] = curVoteTally+1
            
        #output file to hold results            
        outputpath = os.path.join("raw_data","pollResults_"+file.split(".")[0]+".txt")
        
        resultsfile = open(outputpath, "w")
        
        lines = []
        
        #Create output to write
        lines.append("Election Results")
        lines.append("-------------------------")
        lines.append("Total Votes: "+str(totalVotes))
        lines.append("-------------------------")
        
        
        #initialize winner vote count
        winningVotes = 0
        for candidate in candidateList:
            votes = voteCountList[candidateList.index(candidate)]
            pctVotes = (votes/totalVotes)*100
            #check if vote count greater than current leader vote count and assign leader position and leader vote count
            # if yes
            if votes > winningVotes:
                winner = candidate
                winningVotes = votes
            lines.append(candidate+": "+str(round(pctVotes,2))+"% "+"("+str(votes) +")")
        lines.append("-------------------------")
        lines.append("Winner: "+winner)
        
         ##Write the output to file and console
        for line in lines:
            print(line)
            print(line,file=resultsfile)
        
        #new line separator
        print()        
        #close the output file
        resultsfile.close()  

