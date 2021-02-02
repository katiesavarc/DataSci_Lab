import numpy as np
import matplotlib.pyplot as plt


def flux(lum,dist):
    return lum/(4*np.pi*(dist**2))

def make_grid():
    return 0

def calc_std(d_min,d_max,d_steps,xarray,yarray):
    """
    Function that simulates zooming in on a star region 
    (stars have positions defined by the input arrays)
    from d_min to d_max, d_steps times.
    This function produces a historgram for each distance,
    and will plot the surface brightness fluctuations
    as a function of distance.
    Currently, this function assumes uniform brightness.

    Parameters
    ----------
    d_min : float
        closest distance to star region (<1)
    d_max : float
        farthest distance to star region (<=1), 
        cannot be greater than 1.
    d_steps : int
        number of distances to probe within range.
    xarray : Nx1 array of ints
        x-positions of each star in max-size grid
    yarray : Nx1 array of ints
        y-positions of each star in max-size grid
    fluxarray : Nx1 array of fluxes for each star
        flux values of each star in max-size grid
    Returns
    -------
    Plot of brightness fluctuations versus 1/distance.

    """
    
    #check input parameters
    if(d_min>d_max):
        print("minimum distance larger than maximum distance")
        return
    if(d_min>=1 or d_max>1):
        print("out of bounds distance values")
        return
    #if(len(xarray!=len(yarray)!=len(fluxarray))):
    #    print("array lengths not equal")
    #    return
    
    #create an array of distances we want to create points for
    distances = np.linspace(d_min,d_max,d_steps) 
    
    
    #loop through all distances and calculate SBF each time
    sbf_array = [] #array of surface brightness fluctuations
    for d in distances:
        view_limit = get_distance_rescaling(d, field_length)
        hist_out, x_edges, y_edges = make_histogram(xarray, yarray, view_limit, numBins)
        std = np.sqrt(np.mean(hist_out))
        f = flux(luminosity,d)
        sbf = f*std
        sbf_array.append(sbf)
    d_inverse = 1/distances
    plt.subplot(1, 2, 1)
    plt.plot(distances,sbf_array)
    plt.xlabel("d",fontsize=17)
    plt.ylabel("$\sigma_{F_*}$",fontsize=17)
    plt.subplot(1, 2, 2)
    plt.plot(d_inverse,sbf_array)
    plt.xlabel("1/d",fontsize=17)
    plt.ylabel("$\sigma_{F_*}$",fontsize=17)
    plt.tight_layout()
    plt.show()

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

field_length = 128
numBins = 10
N=500

xmax = field_length; ymax = field_length
    
xarray = xmax*np.random.rand(N)
yarray = ymax*np.random.rand(N)

luminosity = 1
d_min = 0.5
d_max = 1
calc_std(d_min,d_max,100,xarray,yarray)      
