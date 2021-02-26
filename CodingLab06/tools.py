import numpy as np
import pandas as pd

def square(arr):
    return arr**2

def get_pi():
    return np.pi

def picky(num):
    if not isinstance(num, (np.float, float, np.int, int)):
        raise TypeError("Must input a number")
def load_dat(filename):
    data_array = pd.read_table(filename,sep=',', header=None)
    time = data_array[0].to_numpy()
    t_0 = np.min(time)
    time = time-t_0 #set smallest time to be t=0
    sidereal_day = 366.242
    time = time*sidereal_day #convert to sidereal day
    s = data_array[1].to_numpy()
    err = data_array[2].to_numpy()
    return time , s , err

