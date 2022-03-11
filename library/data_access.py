import os
from stat import FILE_ATTRIBUTE_NO_SCRUB_DATA
from typing import Dict
from isort import file
import numpy
from csv import DictReader
##from pathlib import Path

from path import Path


def file_output(m,testing,filename = None):
    """
    1) This function is run for each row in the file, which collects data under the same heading into a list
    2) The list of data under each heading is stored in a dictionary for easier access: typically, will expect 
    the first entry in the dictionary to be "Time" values.
    3)Testing = True can be passed in for the purposes of not loading all hte data in a large file: for checking
    if data and values look seem appropriate.
    """

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
            if n > m and testing == True: 
                break
      #  print(row_list)
    return row_list


def file_explorer(m,testing, filenames = None): 
    """
    This function opens the files in a context manager, then passes onto the function file_data which collates the information
    into an appropriate data strcuture.
    """

    directory = 'data' #File directory where .txt files are stored of the wave data
    count = 0
    file_data = []
    #If no filename passed in, will run the explorer for all files in the directory
    if filenames == None:

        for filename in os.scandir(directory):
            if filename.is_file(): #Checking if valid file
                count += 1 
                file_data.append(file_output(m,testing,filename))

    else:
        for filename in filenames:
          #  print(filename)
            count += 1
            file_data.append(file_output(m, testing,filename))
        
    print(count)
    return file_data


#Only if file is directly run: for initial testing

if __name__ == "__main__":
    test_state = True #Running this program only if checking functions
    print(file_explorer(20, test_state, ["/data/ZYB1501.txt"])) #Non-default input - does not scan every file in the directory: only will run for specific listed file/s
    print(file_explorer(20)[1], test_state) #Relative file paths required ["/data/ZYB1501.txt"]) 