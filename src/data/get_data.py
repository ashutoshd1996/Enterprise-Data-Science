import subprocess
import os

import pandas as pd
import numpy as np

from datetime import datetime

import requests
import json
import io

def get_johns_hopkins():
    
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv" # Make sure the url is the raw version of the file on GitHub
    download = requests.get(url).content
    df_jh = pd.read_csv(io.StringIO(download.decode('utf-8')))
    df_jh.to_csv('../data/raw/COVID-19/time_series_covid19_confirmed_global.csv', index = False)


def get_current_data_germany():
    data=requests.get('https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_Landkreisdaten/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')

    json_object=json.loads(data.content)
    full_list=[]
    for pos,each_dict in enumerate (json_object['features'][:]):
        full_list.append(each_dict['attributes'])

    pd_full_list=pd.DataFrame(full_list)
    pd_full_list.to_csv('../data/raw/NPGEO/GER_state_data.csv',sep=';')
    print(' Number of regions rows: '+str(pd_full_list.shape[0]))

if __name__ == '__main__':
    get_johns_hopkins()
    get_current_data_germany()