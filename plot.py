import pandas as pd
import folium
import numpy as np
from folium.plugins import FastMarkerCluster


df = pd.read_csv("./Starbucks_dataset/starbucks_dataset.csv")


df['Latitude'] = pd.to_numeric(df['Latitude'], errors='coerce')
df['Longitude'] = pd.to_numeric(df['Longitude'], errors='coerce')


df_geo = df.dropna(subset=['Latitude', 'Longitude'])

m = folium.Map(
    location=[df_geo['Latitude'].mean(), df_geo['Longitude'].mean()],
    zoom_start=4,
    tiles='CartoDB positron'
)


locations = df_geo[['Latitude', 'Longitude']].values


FastMarkerCluster(data=locations).add_to(m)


m.save("starbucks_fast_cluster_map.html")
print("Map saved! This version should load much faster.")
