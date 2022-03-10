from statistics import mean
from time import time
from venv import create
from isort import file
from data_access import file_explorer
from matplotlib import pyplot as plt
import numpy as np
import math


def wave_information(sea_state_files):   
    states = {}

    for file_ in sea_state_files:
        for key in file_:
            if key == "Time":
                x_values = file_[key]
            else: 
                states[key] = [file_[key], np.mean(file_[key])]
        #First index in list stores list of wave heights over time, Second index stores mean height value 
    
    #Mean time period, and net wave height

    for info in states.values():
        print(info)

        heights = info[0]
        mean_height = info[1]
        crest = []
        trough = []

        #If initially rising: can  infer a crest of a wave is oncoming
        if heights[0] < heights[1]:
            state = "HIGH" 
            hold_h = heights[0]
        #if initially falling: can infer a trough of a wave is oncoming: rate of change is negative
        
        elif heights[1] < heights[0]:
            state = "LOW"
            hold_h = heights[0] 
            crest.append(hold_h) #Initial wave height considered to be peak - collects 1 full wave when completed
            

        #Will have to change this: as it is only for rising heights: not between the peak and the enxt high, but the high and the next low
        
        sum_timedeltas = 0
        timesteps = 0 
        prev_time = 
        time_steps = []
        print("Iterating...")

        for n, h in enumerate(heights[1:],1) :
            print(h)

          
            #Initially, when wav is is rising state, used to detect peak 
            if state == "HIGH":
                if h > hold_h: #No need for further action, if past one full wave 'fall': can terminate iterating through heights list
                    pass
                elif h <= hold_h and n == (len(heights)-1):
                    
                    state = "LOW" #State switched: peak crossed (wave now falling)
                    crest.append(hold_h)
                    trough.append(h) #Ending dip in wave: considered to be falling, complete wave

                elif h <= hold_h:
                    state = "LOW" #State switched: peak crossed (wave now falling)
                    crest.append(hold_h)
                    
                else:
                    trough.append(h)


            #If change of wave progression detected: from rising to falling state
            elif state == "LOW":
                if h < hold_h and n != (len(heights)-1): #if this wave is not the last - if wave is falling at last point, taken to be trough
                    pass
                elif h >= hold_h:
                    state = "HIGH" #State-swtiched: trough crossed (wave now rising)
                    trough.append(hold_h)
                else:
                    trough.append(hold_h)


            #Checking if mean value lies between previous height and current height, and if < prev. but < current - indicates wave rising out of water
            if (hold_h <= mean_height <= h):
                sum_timedeltas += (x_values[n] - prev_t)
                
                time_steps.append(x_values[n]) #For plotting points - vissualise where mean boundary crossed (removed in final))
                timesteps += 1 #Less memory compared to using list
                prev_t = x_values[n]        
            
            hold_h = h #Resetting previous value of h
            
        
            
        
        tz = sum_timedeltas/ timesteps  #1) First required mean value - mean time step between water crossing up mean height
        print(crest)
        print(trough)   #from this bit - data seems to jump up asnd down so much, we might as well consider every consecutive point alternating maxima and minima: try to rewrite the code for this
        #Very small, rippling aves etc....
        
        wave_heights = [(high-low) for high, low in zip(crest, trough)]
        sorted_wave_heights = sorted(wave_heights)
        heights_sum = 0

        for n, height in enumerate(sorted_wave_heights,0):
            if n > math.ceil(len(wave_heights)/3):
                break
            heights_sum += height
        hz = heights_sum/math.ceil(len(wave_heights)/3) #2) Second required mean value

        print("Mean highest 1/3 wave heights: {}, Mea Time step between rising waves: {}".format(hz, tz))

        return "Mean highest 1/3 wave heights: {}, Mea Time step between rising waves: {}".format(hz, tz)

                
            

        
        #Time steps - find differences between consecutive time values, then ass toghether and divide by the total number of iterations of the loop 
        

                
        #Finding the top 30%: subtracting correcponding differences each time the wave - perhaps sort it, check if numpy function to sort



    
    

def graphs_display(sea_state_files, show_plot = False):
    y_values = {} #Library of individual sea_states - wave heights stored as lists
    wave_information

    for file_ in sea_state_files:
        for key in file_:
            if key == "Time":
                x_values = file_[key]
            else: 
                y_values[key] = file_[key]
        #Plotting for each sea state
        for sea_state in y_values.keys():
            print(sea_state)
            plt.plot(x_values, y_values[sea_state], label = str(sea_state))#label = "State: ".format(sea_state))  

        #Setting up plot graphics   
        plt.legend()
        plt.xlabel("Time")
        plt.ylabel("Wave height")   
        
        if show_plot == True: #Pyplot pop-up object may interefere during normal testing - option kept to deactivate (default = False)
            plt.show()
  
     
if __name__ == "__main__":
    limit = 20 # Limiter - for testing, to not overload with large amount of data
    show_plot = True
    graphs_display(file_explorer(limit), show_plot)

limit = 20 # Limiter - for testing, to not overload with large amount of data
show_plot = False
graphs_display(file_explorer(limit), show_plot)
wave_information(file_explorer(limit))
#wave_information(file_explorer(limit))