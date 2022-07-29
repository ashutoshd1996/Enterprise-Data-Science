import pandas as pd
import numpy as np

from datetime import datetime


def store_relational_JH_data():
    path='../data/raw/COVID-19/time_series_covid19_confirmed_global.csv'
    pd_raw_data=pd.read_csv(path)

    pd_data=pd_raw_data.rename(columns={'Country/Region':'country', 'Province/State':'state'})

    pd_data['state']=pd_data['state'].fillna('no')
    pd_data=pd_data.drop(['Lat','Long'],axis=1)
    pd_relational_data=pd_data.set_index(['state','country']) \
                                .T                              \
                                .stack(level=[0,1])             \
                                .reset_index()                  \
                                .rename(columns={'level_0':'date',
                                                   0:'confirmed'},
                                                  )

    pd_relational_data['date']=pd_relational_data.date.astype('datetime64[ns]')
    pd_relational_data.to_csv('../data/processed/COVID_relational_confirmed.csv',sep=';',index=False)

if __name__ == '__main__':

    store_relational_JH_data()