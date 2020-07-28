import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
 

class Filter(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
 
    def fit(self, X, y=None):
        return self
 
    def transform(self, DF, y=None):
        Grouped = DF.groupby(['DAYOFSERVICE','TRIPID'], observed=True)
        DF_filtered = Grouped.filter(first_filter)
        return DF_filtered

def first_filter(x):
    # not sure about the min DIFFTIME?
    if x.DIFFTIME.min() > 7: # drop all routes with any wrong DIFFTIME
        if ~np.isinf(x.VELOCITY).any(): # drop all routes with any wrong VELOCITY
            if len(x) > 5: # drop all short routes with less than 5 stops
                if x.RUNNINGTIME.min() > 0: #drop all routes with any wrong RUNNINGTIME
#                     if x.PROGRNUMBER.reset_index(drop=True).equals(pd.Series(range(x.PROGRNUMBER.min(), x.PROGRNUMBER.max()+1))):
                    # drop discontinuousness routes
#                         return False
#                     else:
                    return True
    else:
        return False