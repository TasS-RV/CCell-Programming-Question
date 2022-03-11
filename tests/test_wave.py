from library.sea_state import wave_information, graphs_display
from library.data_access import file_explorer

def test_wave_information():
    poly = "Some polynomial - to be entered"


    """
    Can perform a variety of test:

    1) Trivial examples of 0 wave height and constant mean water level and infinite
    2) Genearting i.e. traigular waves, or sine waves, where the top 1st value is known,
    and can compare the computed value against the expected value.
    3) Test cases for tz = N/A (infinitely or 0 in reality considering still water, and no waves
    for a flat line as input).
    
    
    """


def test_graphs_display():
    """
    How testing would be done: Generate known oscillating functions, scaling their periods and comparing to the pyplot object 
    output from the main function.

    1)Using math.sin or math,cos (some trig. function) generate a wave series and using plotting function
    Iterating through for series of x, to generate y values

    2)plotobj, = graphs_display() passing in the appropriate
      plot_x = plotobj.get_xdata()
      plot_y = plotobj.get_ydata()
    
    3)The pyplot objects can then be compared against x and y for each generated graph:
    Note: the pyplot object may return a slightly different value (due to differences in decimal accuracy
    compared to the data fed in to generate the plot).#

    We can compare data within an acceptable range, using a function like this:
    for  pltx, realx in zip(plot_x, x):
        assert (abs(pltx, realx) < 0.0001) 

    Or considering the % error between the values to be sufficiently small.
    
    """    

    poly = "Use Sine or Cos wave: find regular period"