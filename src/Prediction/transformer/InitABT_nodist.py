
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd
import pymysql
import datetime

import sys
sys.path.append('/Users/ywq/Dublin_bus/src') # TODO
#from Externel_Data_API.bus_weather_crawler import BusWeatherCrawler


class InitABT_nodist(BaseEstimator, TransformerMixin):
    def __init__(self, line):
        self.weather_DF = pd.read_csv("D:/OneDrive - University College Dublin/Codes/Dublin_bus/src/Data Analysis/2018_daily_inserted.csv", index_col="Unnamed: 0")
        self.weather_DF.date = self.weather_DF.date.astype("datetime64[ns]")
        self.weather_DF.time = self.weather_DF.time.apply(lambda x: datetime.datetime.strptime(x, "%H:%M:%S").time())
        self.line = line
 
    def fit(self, X, y=None):
        return self
 
    def transform(self, DF, y=None):
        unused_cols = ["DATASOURCE", "VEHICLEID", "PASSENGERS", "PASSENGERSIN", "PASSENGERSOUT",
              "DISTANCE", "SUPPRESSED", "JUSTIFICATIONID","LASTUPDATE","NOTE", "PLANNEDTIME_ARR", "PLANNEDTIME_DEP"]
        DF = DF.drop(unused_cols, axis=1)
        DF["ACTUALTIME_ARR_DATETIME"] = DF["DAYOFSERVICE"] + DF["ACTUALTIME_ARR"].apply(seconds_to_timedelta)
        DF["ACTUALTIME_DEP_DATETIME"] = DF["DAYOFSERVICE"] + DF["ACTUALTIME_DEP"].apply(seconds_to_timedelta)
        DF["DAYOFSERVICE"] = DF["DAYOFSERVICE"].astype("datetime64[ns]") # Debug
        DF["WEEK_DAY"] = DF["DAYOFSERVICE"].dt.dayofweek
        DF["PERIOD"] = DF["ACTUALTIME_ARR_DATETIME"].apply(time_to_periods)

        DF_merged = pd.merge(DF, self.weather_DF, left_on=['DAYOFSERVICE','PERIOD'], \
                right_on=['date','time'], how='left').drop(['date','time'], axis=1)

        DF_merged['DWELLTIME'] = DF_merged["ACTUALTIME_DEP"] - DF_merged["ACTUALTIME_ARR"]
        DF_merged["STARTEND"] = DF_merged.groupby(['DAYOFSERVICE','TRIPID'])['STOPPOINTID'].apply(lambda x:x.shift(1)+'_'+x)
        DF_merged['DIFFTIME'] = DF_merged.groupby(['DAYOFSERVICE','TRIPID'])['ACTUALTIME_ARR'].apply(lambda x:x.diff(1))

        # START_END_dist = Get_Distance(self.line, DF_merged)

        # DF_merged = pd.merge(DF_merged, START_END_dist, on=['STARTEND'], how='left')

        t = DF_merged.groupby(['DAYOFSERVICE','TRIPID']).apply(lambda x:x["DIFFTIME"] -x.shift(1)["DWELLTIME"])
        # There is a bug from pandas 0.12, solution is:
        # reset twice the index
        t = t.reset_index(level=0, drop=True)
        t = t.reset_index(level=0, drop=True)
        DF_merged['RUNNINGTIME'] = t
        del(t)

        # t = DF_merged.groupby(['DAYOFSERVICE','TRIPID']).apply(lambda x:x["DISTANCE"] / x["RUNNINGTIME"])
        # # There is a bug from pandas 0.12, solution is:
        # # reset twice the index
        # t = t.reset_index(level=0, drop=True)
        # t = t.reset_index(level=0, drop=True)
        # DF_merged["VELOCITY"] = t
        # del(t)

        DF = DF_merged
        del DF_merged

        cols_to_datetype = ["DAYOFSERVICE","ACTUALTIME_ARR_DATETIME","ACTUALTIME_DEP_DATETIME"]
        for i in cols_to_datetype:
            DF[i] = DF[i].astype('datetime64[ns]')
            
        cols_to_cat = ["TRIPID","STOPPOINTID", "WEEK_DAY","condition"]#,"PERIOD"
        for i in cols_to_cat:
            DF[i] = DF[i].astype('category')

        DF.PERIOD = DF.PERIOD.apply(lambda x: str(x)) # PERIOD to str

        return DF

def seconds_to_timedelta(x):
    """convert seconds to timedelta"""
    return datetime.timedelta(seconds=x)

def time_to_periods(x):
    """convert time to periods defined"""
    if x.minute < 30:
        m = 0
    else:
        m = 30
    return datetime.time(x.hour,m)