import rasterio
import numpy
import pandas 

def DamageScanner(landuse_map,inun_map,curve_path,maxdam_path,cellsize=100):
    """
    Raster-based implementation of a direct damage assessment.
    
    Arguments:
        *landuse_map* : GeoTiff with land-use information per grid cell. Make sure 
        the land-use categories correspond with the curves and maximum damages 
        (see below). Furthermore, the resolution and extend of the land-use map 
        has to be exactly the same as the inundation map.
     
        *inun_map* : GeoTiff with inundation depth per grid cell. Make sure 
        that the unit of the inundation map corresponds with the unit of the 
        first column of the curves file.
     
        *curve_path* : File with the stage-damage curves of the different 
        land-use classes. Can also be a pandas DataFrame or numpy Array.
     
        *maxdam_path* : File with the maximum damages per land-use class 
        (in euro/m2). Can also be a pandas DataFrame or numpy Array.
     
        
    Returns:    
     *damagebin* : Table with the land-use class numbers (1st column) and the 
     damage for that land-use class (2nd column).
     
     
    """      
        
    # load land-use map
    if isinstance(landuse_map,str):
        with rasterio.open(landuse_map) as src:
            landuse = src.read()[0,:,:]
    else:
        landuse = landuse_map.copy()
    
    
    # Load inundation map
    if isinstance(inun_map,str):
        with rasterio.open(inun_map) as src:
            inundation = src.read()[0,:,:]
    else:
        inundation = inun_map.copy()
    
    inundation = numpy.nan_to_num(inundation)        

    # set cellsize:
    if isinstance(landuse_map,str) | isinstance(inun_map,str):
        cellsize = src.res[0]*src.res[1]


    # Load curves
    if isinstance(curve_path, pandas.DataFrame):
        curves = curve_path.values   
    elif isinstance(curve_path, numpy.ndarray):
        curves = curve_path
    elif curve_path.endswith('.csv'):
        curves = pandas.read_csv(curve_path).values

    #Load maximum damages
    if isinstance(maxdam_path, pandas.DataFrame):
        maxdam = maxdam_path.values 
    elif isinstance(maxdam_path, numpy.ndarray):
        maxdam = maxdam_path
    elif maxdam_path.endswith('.csv'):
        maxdam = pandas.read_csv(maxdam_path,skiprows=1).values
        
    # Speed up calculation by only considering feasible points
    inun = inundation * (inundation>=0) + 0
    inun[inun>=curves[:,0].max()] = curves[:,0].max()
    waterdepth = inun[inun>0]
    landuse = landuse[inun>0]

    # Calculate damage per land-use class for structures
    numberofclasses = len(maxdam)
    alldamage = numpy.zeros(landuse.shape[0])
    damagebin = numpy.zeros((numberofclasses, 4,))
    for i in range(0,numberofclasses):
        n = maxdam[i,0]
        damagebin[i,0] = n
        wd = waterdepth[landuse==n]
        alpha = numpy.interp(wd,((curves[:,0])),curves[:,i+1])
        damage = alpha*(maxdam[i,1]*cellsize)
        damagebin[i,1] = sum(damage)
        damagebin[i,2] = len(wd)
        if len(wd) == 0:
            damagebin[i,3] = 0
        else:
            damagebin[i,3] = numpy.mean(wd)
        alldamage[landuse==n] = damage

    # create pandas dataframe with output
    loss_df = pandas.DataFrame(damagebin.astype(float),columns=['landuse','losses','area','avg_depth']).groupby('landuse').sum()
    
    # return output
    return loss_df.sum().values[0],loss_df