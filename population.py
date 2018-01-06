
import matplotlib.pyplot as plt
import matplotlib.cm
import pandas as pd
import numpy as np

from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize

fig, ax = plt.subplots(figsize=(15,30))


m = Basemap(resolution='c', # c, l, i, h, f or None
            projection='merc',
            lat_0=54.5, lon_0=-4.36,
            llcrnrlon=65, llcrnrlat= 5.26, urcrnrlon=97.88, urcrnrlat=38)


m.drawmapboundary(fill_color='#46bcec')
m.fillcontinents(color='#f2f2f2',lake_color='#46bcec')
m.drawcoastlines()

data = {'ST_NM': ["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat",
"Haryana","Himachal Pradesh","Jammu & Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh",
"Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim",
"Tamil Nadu","Telangana","Tripura","Uttarakhand","Uttar Pradesh","West Bengal"],'pop': [49386799,1383727,31205576,104099452,25545198,1458545,60439692,25351462,6864602,
12541302,32988134,61095297,33406061,72626809,112374333,2855794,2966889,1097206,1978502,41974218,
27743338,68548437,610577,72147030,35193978,3673917,10086292,199812341,91276115],
'pos': [(14.7504291,78.57002559),(27.10039878,93.61660071),(26.7499809,94.21666744),(25.78541445,87.4799727),
(22.09042035,82.15998734),(15.491997,73.81800065),(22.2587, 71.1924),(28.45000633,77.01999101),(31.10002545,77.16659704),
(34.29995933,74.46665849),(23.80039349,86.41998572),(12.57038129,76.91999711),(8.900372741,76.56999263),
(21.30039105,76.13001949),(19.25023195,73.16017493),(24.79997072,93.95001705),(25.57049217,91.8800142),
(23.71039899,92.72001461),(25.6669979,94.11657019),(19.82042971,85.90001746),(31.51997398,75.98000281),
(26.44999921,74.63998124),(27.3333303,88.6166475),(12.92038576,79.15004187),(18.1124, 79.0193),
(23.83540428,91.27999914),(30.32040895,78.05000565),(27.59998069,78.05000565),(22.58039044,88.32994665)]}
df = pd.DataFrame(data)


"""def plot_area(pos):
    pop = df.loc[df.pos == pos]['pop']
    x, y = m(pos[1], pos[0])
    size = (pop/10000000)
    m.plot(x, y, 'o', markersize=size, color='#444444', alpha=0.8)
    
df.pos.apply(plot_area)"""

m.readshapefile('/home/tejaswi/Desktop/vsaitejaswie.github.io/states', 'areas')

#print(m.areas)


df_poly = pd.DataFrame({
        'shapes': [Polygon(np.array(shape), True) for shape in m.areas],
        'ST_NM': [ST_NM['ST_NM'] for ST_NM in m.areas_info]
    })


df_poly = df_poly.merge(df, on='ST_NM', how='left')

cmap = plt.get_cmap('Greens')   
pc = PatchCollection(df_poly.shapes, zorder=2)
norm = Normalize()

pc.set_facecolor(cmap(norm(df_poly['pop'].fillna(0).values)))
ax.add_collection(pc)


mapper = matplotlib.cm.ScalarMappable(norm=norm, cmap=cmap)

mapper.set_array(df_poly['pop'])
plt.colorbar(mapper, shrink=1)

plt.title("God knows what!")
plt.show()