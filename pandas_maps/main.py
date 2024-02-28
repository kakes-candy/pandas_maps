import logging
from config.logging_config import log_config
import pandas as pd
import seaborn as sns
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
from shapely.geometry import Point

# -------------------------------------------------------------------------------------------------------
# LOGGING Initialiseren
# -------------------------------------------------------------------------------------------------------
logging.config.dictConfig(log_config)
rootlogger = logging.getLogger()
rootlogger.setLevel(logging.ERROR)
log_filename = log_config.get('handlers').get('file').get('filename')

rootlogger.info(f"logger initialised, logfilename: {log_filename}")


# Data
shapefile = 'pandas_maps/data/wijkbuurtkaart_2023_v1/wijken_2023_v1.shp'
map_df = gpd.read_file(shapefile)
print(map_df.columns)
map_df = map_df.to_crs(epsg=3395)

# Plot the default map
# map_df.plot()


lon = 4.9610717
lat = 52.5488542


fig = plt.figure(figsize=(100, 50))
ax2 = map_df.plot(figsize=(100, 50), edgecolor='black', facecolor="none")

ax2.figure.savefig("alone.png", format='png')

adress = [Point((lon, lat))]

adress_df = gpd.GeoDataFrame(geometry = adress, crs =  4326)

adress_df =adress_df.to_crs(3395)

combined = adress_df.plot(ax = ax2, markersize = 20, color = 'red',marker = '*',label = 'Delhi')



combined.figure.savefig("combined.png", format='png')





