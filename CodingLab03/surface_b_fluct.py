import numpy as np
import matplotlib.pyplot as plt

def main():
    #This will be replaced with Ingrid's code
    N = 500
    field_length = 128
    xmax = field_length; ymax = field_length
    
    x_list = xmax*np.random.rand(N)
    y_list = ymax*np.random.rand(N)
    
    plt.figure()
    plt.plot(x_list, y_list, 'o')
    
    #Settings that Katie can use for my function
    distance = 0.9
    numBins = 20
    plot_density = True
    
    #My function
    density_hist = get_density_field(distance, field_length, x_list, y_list, numBins, plot_density)
    std_density = np.std(density_hist)
    #Katie will use my function in a for loop over a range of distances
    
    #Katie will plot std_density vs distance
    
    
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
#def make_grid():

#def calc_std():

main()

