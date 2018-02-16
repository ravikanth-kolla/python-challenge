#Assess the passage for each of the following:
#
#Approximate word count
#
#Approximate sentence count
#
#Approximate letter count (per word)
#
#Average sentence length (in words)
#
#As an example, this passage:
#
#“Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood 
#with his great sword point upwards, the red raiment of his office flapping around 
#him like the red wings of an archangel. And the King saw, he knew not how, something 
#new and overwhelming. The great green trees and the great red robes swung together in 
#the wind. The preposterous masquerade, born of his own mockery, towered over him and 
#embraced the world. This was the normal, this was sanity, this was nature, and he 
#himself, with his rationality, and his detachment and his black frock-coat, he was 
#the exception and the accident - a blot of black upon a world of crimson and gold.”
#
#...would yield these results:
#
#Paragraph Analysis
#-----------------
#Approximate Word Count: 122
#Approximate Sentence Count: 5
#Average Letter Count: 4.56557377049
#Average Sentence Length: 24.4

#Use this to split 
#re.split("(?&lt;=[.!?]) +", paragraph)


import re

import os



    
#list of data files that you can add more to if required
fileList = ["paragraph_1.txt","paragraph_2.txt"]
for file in fileList:
    #assumes data files exist in the directory raw_data which is at the same level
    #as the script
    txtpath = os.path.join("raw_data",file)
    with open(txtpath, 'r') as text:

        #print(text)
    
        # Store all of the text inside a variable called "lines"
        lines = text.read()
        
        
        #Found this regex that works best on stackoverflow
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', lines)
        
        #Assume space separates words - count hyphenated words as one word
        words = re.split(r' ', lines)
        
        
       
        
        letterCount = 0
        for word in words:
            letterCount = letterCount + len(word)
       
       
        
        
        #create and open output file to write resuts to
        outputpath = os.path.join("raw_data",file.split(".")[0] + "_Analysis.txt")

        lines = []
    
        resultsfile = open(outputpath, "w")
    
        lines.append("Paragraph Analysis")
        lines.append("-----------------")
        lines.append("Approximate Word Count:: "+str(len(words)))
        lines.append("Approximate Sentence Count: "+str(len(sentences)))
        lines.append("Average letter count: "+ str(round(letterCount/len(words),2)))
        lines.append("Average Sentence Length: "+ str(round(len(words)/len(sentences),2)))
        
         ##Write the output to file and console
        for line in lines:
            print(line)
            print(line,file=resultsfile)
        
        #new line
        print()
    
        #close the file
        resultsfile.close()