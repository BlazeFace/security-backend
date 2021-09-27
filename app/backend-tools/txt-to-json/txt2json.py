"""
=== BIT/CS/PSCI 4164 FALL 2021 ===
===      Security Planner      ===
===       Backend Support      ===

Python program to convert a text file 
to JSON format

@author
    Camden Landis (craine)

@version
    09.09.2021

USAGE:
    >> python3 txt2json.py

"""
# --------------------------------------------------------------------------

# IMPORT(S)
import json

# --------------------------------------------------------------------------  

# the file to be converted
filename = 'content.txt'
  
# resultant dictionary
dict_final = {}
  
# fields in the sample file 
fields = ['device', 'threat level', 'popularity']
  
with open(filename) as text_file:
      
    # count variable data object
    content_count = 1
      
    for line in text_file:
          
        # reading line by line from the text file
        description = list( line.strip().split(None, 3)) # update based on 
							 # field number
          
        # for output see below
        print(description) 
          
        # for automatic creation of content object
        identity = str(content_count)

        # temporary dictionary
        dict_temp = {}

        i = 0
        while (i < len(fields)):  
            # creating dictionary for each object
            dict_temp[fields[i]]= description[i]
            i += 1
                  
        # appending the record of each object
        # to the main dictionary
        dict_final[identity] = dict_temp
        content_count += 1
  
  
# creating json file        
out_file = open("content.json", "w")
json.dump(dict_final, out_file, indent = 4)
out_file.close()

# --------------------------------------------------------------------------
