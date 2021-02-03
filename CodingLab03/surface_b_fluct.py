import numpy as np
import matplotlib.pyplot as plt
    
    
def make_histogram(x_list, y_list, view_limit, numBins):
    """
    Make a 2D histogram of star density on our view field
    
    Inputs:
        x_list, y_list: (Nx1 arrays) contain the x & y coordinates of all stars
        view_limit: (int) upper limit to set the field of view. Lower limit is always zero,
            meaning our viewing window will always be in the bottom-left corner of the overall field
        numBins: (int) number of bins to use in each dimension of the histogram
    Outputs:
        density_hist: (numBins x numBins array) histogram of the star density
        xedges, yedges: (numBins+1 x 1 arrays) list of edge locations for the histogram bins
    """
    
    #Check if the number of elements is less than the number of bins
    elements_in_view = sum((x_list<view_limit)*(y_list<view_limit))
    #Print an error statement if the number of elements falls below this threshold
    if elements_in_view < numBins:
        print('Number of elements in field of view is less than the number of bins.')
    
    #Get the view limits on which to generate our histogram
    range_hist = [[0, view_limit], [0, view_limit]]
    
    #Generate the 2D histogram
    density_hist, xedges, yedges = np.histogram2d(y_list, x_list, bins = numBins, range=range_hist, density=True)

    return density_hist, xedges, yedges

def get_distance_rescaling(distance, field_length):
    """
    Given the distance at which we want to observe (as a ratio compared to the
    full field of view at distance=1), calculate the field of view limits
    """

    #The field of view side length is proportional to distance^2
    rescaling = distance**2
    #Rescale the view size by the rescaling factor, and truncate to an integer value
    view_limit = int(rescaling*field_length)
    
    return view_limit

def get_density_field(distance, field_length, x_list, y_list, numBins, plot_density):
    """
    Take a distance and list of star coordinates and return the density field histogram
    corresponding to the field of view at that distance
    """
    #Get the upper limit for viewing field coordinates
    view_limit = get_distance_rescaling(distance, field_length)
    
    #Get the 2D histogram of star density in the specified viewing field
    density_hist, xedges, yedges = make_histogram(x_list, y_list, view_limit, numBins)
    
    #Option to generate a heatmap plot of the star density
    if plot_density:
        X,Y = np.meshgrid(xedges, yedges)
        plt.figure()
        plt.pcolormesh(X, Y, density_hist)
        plt.title('Star Density at distance scale ' + str(distance))
        plt.xlabel('X')
        plt.ylabel('Y')
        
    return density_hist
   
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

