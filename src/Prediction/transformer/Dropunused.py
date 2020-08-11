import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
 

class Dropunused(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
 
    def fit(self, X, y=None):
        return self
 
    def transform(self, DF, y=None):
        used = ["DAYOFSERVICE","TRIPID", "WEEK_DAY", "PERIOD", "condition", "DWELLTIME", "STARTEND", "DISTANCE", "VELOCITY"]
        return DF[used]
