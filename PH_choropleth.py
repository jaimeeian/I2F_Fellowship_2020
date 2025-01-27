import folium
import pandas as pd
from IPython.display import HTML, display
import json

def ProvinceSort(file):
    
    data = pd.read_csv(file)

    try:
        data_byProvince = data['Province/State'].value_counts()
        data_byProvince = pd.DataFrame([data_byProvince]).T
        data_byProvince = data_byProvince.rename(columns={'Province/State':'# of objects'})
        data_byProvince = data_byProvince.reset_index()
        data_byProvince = data_byProvince.rename(columns={'index':'Province/State'})
        return data_byProvince

    except:
        return "No column 'Province/State'"



class PH_Choropleth:

    def __init__(self, geo, data):
        self.geo = geo
        self.data = data
        self.PH_map = folium.Map([8.0106, 124.2977], zoom_start=7)

        folium.Choropleth(geo_data=geo, 
                          name='choropleth', 
                          data=data,
                          columns=['Province/State', '# of objects'], 
                          key_on='feature.properties.PROVINCE',
                          fill_color='YlGn',
                          fill_opacity=0.7,
                          line_opacity=0.2,
                          legend_name='# of objects').add_to(self.PH_map)

        folium.LayerControl().add_to(self.PH_map)

    def save(self, filename):
        self.PH_map.save(filename)

import os
import glob

def manyMaps(directory, geo):
    files = glob.glob(directory+'/*.csv')
    for file in files:
        data = ProvinceSort(file)
        map = PH_Choropleth(geo, data)
        outfile = file[:-9]+'_map.html'
        map.save(outfile)
        print(file[:-9], ': done')

class allData:
    def __init__(self, directory):
        self.sortedData(directory)

    def sortedData(self, loc):
        files = glob.glob(loc+'/*.csv')
        for file in files:
            if file==files[0]:
                data = ProvinceSort(file)
                print(data)
            else:
                data2 = ProvinceSort(file)
                print(data2)
                data = data.append(data2, ignore_index=True)

        return data


def spellChecker(province_json, csv_data):
    with open(province_json, 'r') as f:
        official_data = json.load(f)
    
    

    features = official_data['features']
    official_provinces = []
    for province in features:
        official_provinces.append(province['properties']['PROVINCE'])
    
    print(official_provinces.casefold())
    
    
