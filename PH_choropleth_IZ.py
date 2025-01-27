import folium
import pandas as pd


PH_geo = f'geojsonph/Province/Provinces.json'
IZ_collections = f'IZ_data_byProvince.csv'
IZ_data = pd.read_csv(IZ_collections)

PH_map = folium.Map([8.0106, 124.2977], zoom_start=7)

folium.Choropleth(geo_data=PH_geo, 
                  name='choropleth', 
                  data=IZ_data,
                  columns=['Province/State', '# of objects'], 
                  key_on='feature.properties.PROVINCE',
                  fill_color='YlGn',
                  fill_opacity=0.7,
                  line_opacity=0.2,
                 legend_name='# of objects').add_to(PH_map)

folium.LayerControl().add_to(PH_map)

PH_map
