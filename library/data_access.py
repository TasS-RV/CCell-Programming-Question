import os
from stat import FILE_ATTRIBUTE_NO_SCRUB_DATA
from typing import Dict
from isort import file
import numpy
from csv import DictReader
##from pathlib import Path

from path import Path


def file_output(m,filename = None):

    with open(filename, 'r') as f:
            
        n = 0 # Temporary limiter for number of data

        row_list = {}
        for row in DictReader(f, delimiter = "\t"):
            
            state = True
            if None or '' in row.values():
                state = False #If inconsistent values at this timestep, None or Blank, skip over this Row
                
            #Skips entire row if any inconsistency in data,. or blank data point (seen with first line)
            for key in row:
                #Conversion into int, collated into a list of numbers for each 'header'
                if key not in row_list.keys() and state == True:
                    row_list[key] = [float(row[key])]
                elif state == True:
                    row_list[key].append(float(row[key]))                    

            n +=1
            if n > 20:
                break
      #  print(row_list)

    return row_list


def file_explorer(m,filenames = None): 
    directory = 'data' #File directory where .txt files are stored of the wave data
    count = 0
    file_data = []
    #If no filename passed in, will run the explorer for all files in the directory
    if filenames == None:

        for filename in os.scandir(directory):
            if filename.is_file(): #Checking if valid file
                count += 1 
                file_data.append(file_output(m,filename))

    else:
        for filename in filenames:
          #  print(filename)
            count += 1
            file_data.append(file_output(m,filename))
        
    print(count)
    
    return file_data


#print(file_explorer(20)[1]) #Inquire about relative file paths ["/data/ZYB1501.txt"]) 