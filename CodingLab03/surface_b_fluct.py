def main():

def make_histogram():

def make_grid():

def calc_std(d_min,d_max,d_steps,xarray,yarray,fluxarray):
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
    #loop
