import random
import matplotlib.pyplot as plt

def main():
   
#assuming the range is from 0 - xlim/ylim
#N is number of points you want to generate
def Generate_data(xlim,ylim,N):
    x_coord=[]
    y_coord=[]
    for i in range(N):
        x_coord.append(random.uniform(0,xlim))
        y_coord.append(random.uniform(0,ylim))
    return x_coord,y_coord

def make_histogram():

#nx and ny are the number of pixels in x coord and in y coord
#ex: nx = 3 we want the xlim to be split into three pixels
def make_grid(x_coord,y_coord,xlim,ylim,nx,ny):
    x_pixels = xlim/nx
    y_pixels = ylim/ny
    for i in range(nx+1):
        plt.vlines(x_pixels*i,0,ylim,colors='black',linestyles='solid')
    
    for j in range(ny+1):
        plt.hlines(y_pixels*j,0,xlim,colors='black',linestyles='solid')
    
    #plotting the data
    plt.scatter(x_coord,y_coord,c='orange',marker="*") #should plot the points as little stars


def calc_std():