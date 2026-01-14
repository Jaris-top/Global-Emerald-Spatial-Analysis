Python 3.13.9 (v3.13.9:8183fa5e3f7, Oct 14 2025, 10:27:13) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> import pandas as pd
... import geopandas as gpd
... from shapely.geometry import Point
... 
... print("读取csv")
... data = pd.read_csv('emerald (10m).csv')
... point_list = []
... 
... for index, row in data.iterrows():
...     x = row['Longitude']
...     y = row['Latitude']
...     p = Point(x, y)
...     point_list.append(p)
... 
... gdf = gpd.GeoDataFrame(data, geometry=point_list)
... gdf.crs = "EPSG:4326"
... 
... print("读取分界shp")
... shp = gpd.read_file('ne_10m_admin_1_states_provinces.shp')
... 
... gdf = gdf.to_crs(epsg=3857)
... shp = shp.to_crs(epsg=3857)
... 
... print("计算距离")
... distances = []
... 
... for i in range(len(gdf)):
...     if i % 10 == 0:
...         print(i)
...     current_point = gdf.geometry.iloc[i]
...     d = shp.boundary.distance(current_point)
...     min_dist = d.min()
...     final_km = min_dist / 1000
...     distances.append(final_km)
... 
... gdf['dist_to_bound_km'] = distances
... 
print("保存")
gdf.to_csv('final emerald (10m).csv', index=False)

print(gdf.head())
