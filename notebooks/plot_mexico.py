import pandas as pd
import matplotlib.pyplot as plt
import descartes
import geopandas

# 0          Aguascalientes
# 1         Baja California
# 2     Baja California Sur
# 3                Campeche
# 4                 Chiapas
# 5               Chihuahua
# 6                Coahuila
# 7                  Colima
# 8        Distrito Federal
# 9                 Durango
# 10         Edo. de México
# 11             Guanajuato
# 12               Guerrero
# 13                Hidalgo
# 14                Jalisco
# 15              Michoacán
# 16                Morelos
# 17                Nayarit
# 18             Nuevo León
# 19                 Oaxaca
# 20                 Puebla
# 21              Querétaro
# 22           Quintana Roo
# 23        San Luis Potosí
# 24                Sinaloa
# 25                 Sonora
# 26                Tabasco
# 27             Tamaulipas
# 28               Tlaxcala
# 29               Veracruz
# 30                Yucatán
# 31              Zacatecas

def plot_mexico(gdf, column='cantidad', cmap='Oranges', figsize = (30, 16)):
    gdf['coords'] = gdf['geometry'].apply(lambda x: x.representative_point().coords[:])
    gdf['coords'] = [coords[0] for coords in gdf['coords']]
    plt = gdf.plot(column=column, legend=True, cmap=cmap, edgecolor='gray', figsize = figsize);
    arrowprops = dict(color='black', width=1, headwidth=7, shrink=0.05)

    arrow_states = ['Distrito Federal', 'Edo. de México', 'Querétaro', 'Tlaxcala', 'Morelos', \
                    'Aguascalientes', 'Puebla', 'Veracruz']
    plt.annotate(s='Distrito Federal', xy=(gdf['coords'][8][0]-0.2,gdf['coords'][8][1]-0.1), \
                 xytext=(gdf['coords'][8][0]+4.1,gdf['coords'][8][1]+2.1), arrowprops=arrowprops);
    plt.annotate(s='Edo. de México', xy=gdf['coords'][10], \
                 xytext=(gdf['coords'][10][0]+4,gdf['coords'][10][1]+3), arrowprops=arrowprops); 
    plt.annotate(s='Querétaro', xy=gdf['coords'][21], \
                 xytext=(gdf['coords'][21][0]+4,gdf['coords'][21][1]+3), arrowprops=arrowprops);  
    plt.annotate(s='Tlaxcala', xy=gdf['coords'][28], \
                 xytext=(gdf['coords'][28][0]+4,gdf['coords'][28][1]+1), arrowprops=arrowprops); 
    plt.annotate(s='Morelos', xy=gdf['coords'][16], \
                 xytext=(gdf['coords'][16][0]-5,gdf['coords'][16][1]-3), arrowprops=arrowprops); 
    plt.annotate(s='Aguascalientes', xy=gdf['coords'][0], \
                 xytext=(gdf['coords'][0][0]-6,gdf['coords'][0][1]-2), arrowprops=arrowprops); 
    plt.annotate(s='Puebla', xy=gdf['coords'][20], \
                 xytext=(gdf['coords'][20][0]-2,gdf['coords'][20][1]-4), arrowprops=arrowprops);
    plt.annotate(s='Veracruz', xy=(gdf['coords'][29][0]+1.2,gdf['coords'][29][1]-1.9))
    
    for idx, row in gdf.iterrows():
        if row['ADMIN_NAME'] not in arrow_states:
            plt.annotate(s=row['ADMIN_NAME'], xy=row['coords'], horizontalalignment='center')