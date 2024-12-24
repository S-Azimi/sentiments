from mpl_toolkits.basemap import Basemap

# Set up Basemap instance
m = Basemap(projection='lcc', resolution='h',
            lat_0=37.5, lon_0=-119,
            llcrnrlon=-119, llcrnrlat=36,
            urcrnrlon=-118, urcrnrlat=37)

m.drawcoastlines()
m.drawcountries()

# Convert your data coordinates to map coordinates if necessary
x, y = m(lons, lats)  # lons and lats are your longitude and latitude arrays

# Create the heatmap on top of the map
heatmap = m.imshow(data, cmap='viridis', alpha=0.5)
plt.colorbar(heatmap)
plt.title('Heatmap on Map')
plt.show()



