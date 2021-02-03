import random
import matplotlib.pyplot as plt

def main():
   

def Generate_data(xmax,ymax,N):
    """
    Randomly generates (x,y) coordinates for star and their luminosity
    
    Inputs:
        xmax,ymax: the maximum point on the axis
        N: number of data point stars wanted 
    Outputs:
        x_list: the x coordinate of a star
        y_list: the y coordinate of a star
        star_lum: the current luminosity associated to each star
    """
    x_list=[]
    y_list=[]
    star_lum = np.full((1,N),1) #stays the same
    star_flux(star_lum,1)

    for i in range(N):
        x_list.append(random.uniform(0,xmax))
        y_list.append(random.uniform(0,ymax))
    return x_list,y_list,star_lum

def star_flux(star_lum,distance):
    """
    Generates the flux for the input of luminosities and at what scale distance
    
    Inputs:
        star_lum: the luminosities of the stars
        d: distance
    Outputs:
        star_flux: the flux of each star
    """
    star_flux = star_lum/4*np.pi*(distance**2) #recalculate for change in d
    return star_flux


def make_histogram():

#nx and ny are the number of pixels in x coord and in y coord
#ex: nx = 3 we want the xlim to be split into three pixels
def make_grid(x_list,y_list,xmax,ymax,numBins_x,numBins_y):
    """
    Makes the grid of where each star fall in our grid
    
    Inputs:
        x_list: x coordinates of a star
        y_list: y coordinates of a star
        max,ymax: the maximum point on the axis
        numBins_x: number of bins wanted in x-axis
        numBins_y: number of bins wanted in y-axis
    """

    x_pixels = xlim/numBins_x
    y_pixels = ylim/numBins_y
    for i in range(nx+1):
        plt.vlines(x_pixels*i,0,ylim,colors='black',linestyles='solid')
    
    for j in range(ny+1):
        plt.hlines(y_pixels*j,0,xlim,colors='black',linestyles='solid')
    
    #plotting the data
    plt.scatter(x_list,y_list,c='orange',marker="*") #should plot the points as little stars


def calc_std():
