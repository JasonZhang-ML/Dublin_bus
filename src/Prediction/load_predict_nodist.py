## run this script under the location with pkl files.
import joblib
import numpy as np
import pandas as pd
import os
from sklearn.svm import SVR, LinearSVR
from scipy import stats
from fitter import Fitter
from pykalman import KalmanFilter


class average_model():
    def __init__(self):
        pass
    def fit(self, X, y):
        self.y = y
        return self
    def predict(self, X):
        return self.y.mean()

def predict_list(line, direction, dayofweek, period, weather,stop_list=None, model=0, dynamic=None):
    """
    Input
        line: routeid; direction: 1 or 2; stop_list: list of stopids
        dayofweek [0:6]; period: '05:00:00'-'00:00:00'; weather: 'Fair' or 'Bad'
        model(int): from 0 to ...
    
    Output
        result_cum
    """
    
    pkl_name = str(line) + "_" + str(direction) + "_n.pkl"
    if os.path.exists(pkl_name):
        DF = joblib.load(pkl_name)
    else:
        # TODO: get the pkl
        return None
    # Choose the first trip
    if stop_list == None:
        first_row = DF.iloc[0]
        h = DF[DF.eval("DAYOFSERVICE == '{}' and TRIPID == '{}'".format(first_row["DAYOFSERVICE"],first_row["TRIPID"]))].STARTEND.dropna(axis=0,how='any')
        stop_list = []
        for i in h:
            stop_list.append(i.split('_')[0])
        stop_list.append(h.iloc[-1].split('_')[1])
        
    results = [0,]
    for i in range(0,len(stop_list)-1):
        results.append(predict_every_two(stop_list[i],stop_list[i+1],dayofweek,period,weather,DF, model, dynamic))
    result_cum = pd.DataFrame(np.cumsum(results), stop_list, columns=["Time cumsum"])
    return result_cum


def predict_every_two(start, end, dayofweek, period, weather, DF, model, dynamic):
    # dayofweek [0:6]; period: '05:00:00'-'00:00:00'; weather: 'Fair' or 'Bad'
    start_end = str(start) + '_' + str(end)
    DF_whole = DF[DF.eval("STARTEND == '{}'".format(start_end))].copy()
    peak_periods = ['7:00:00', '7:30:00','8:00:00','8:30:00','9:00:00','16:00:00','16:30:00','17:00:00','17:30:00','18:00:00']
    DF_whole["PERIOD"] = DF_whole.apply(lambda x: 1 if x.PERIOD in peak_periods else 0, axis=1) # peak 1, offpeak 0
    DF_whole["WEEK_DAY"] = DF_whole.apply(lambda x: 1 if x.WEEK_DAY > 4 else 0, axis=1) # weekend 1 , weekday 0
    DF_whole["condition"] = DF_whole.apply(lambda x: 1 if x.condition == "Fair" else 0, axis=1) # Fair 1, Bad 0

    X = DF_whole[["WEEK_DAY","PERIOD","condition"]]
    # y = DF_whole["VELOCITY"]
    y = DF_whole["RUNNINGTIME"]
    models =[
        (LinearSVR(epsilon=1.5)),
        (SVR(kernel="poly", degree=2, C=100, epsilon=0.1)),
        (average_model())]
    model_selected = models[model]
    model_selected.fit(X,y)
    
    
    # transform dayofweek, period, weather
    x1 = [1 if period in peak_periods else 0]
    x2 = [1 if dayofweek > 4 else 0]
    x3 = [1 if weather == "Fair" else 0]

#     f = DF_whole[DF_whole.eval("PERIOD == '{}' and WEEK_DAY == {}".format(period,dow))]
    runningtime_predicted = model_selected.predict(pd.DataFrame([x1,x2,x3]).T)

    # fit dwell time with gamma distibution and predict it randomly based on fitted distribution
    ## limit size of data to reduce runnning time
    if len(DF_whole["DWELLTIME"]) > 501:
        data = DF_whole["DWELLTIME"].iloc[:500]
    else:
        data = DF_whole["DWELLTIME"]

    f = Fitter(data,distributions=['gamma'], timeout=6000)
    f.fit()

    param = f.fitted_param['gamma']
    rv = stats.gamma(a=param[0],loc=param[1],scale=param[2])
    dwelltime_predict = rv.rvs(1)
    difftime_predicted = runningtime_predicted + dwelltime_predict
    # kalman filter to adjust the prediction result
    if dynamic != None:
        initial_state = np.asarray([difftime_predicted])
        measurements = np.asarray([initial_state]) # which should be repalced by realtime result
        # realtime = ..... # TODO:the difftime of last bus that has just traveled along the road segment with multiple bus routes.
        # measurements = np.asarray([realtime])

        kf = KalmanFilter(transition_matrices=[1], observation_matrices=[1], initial_state_mean=initial_state,n_dim_obs=1)
        # kf = kf.em(measurements)
        (filtered_state_means, filtered_state_covariances) = kf.filter(measurements)
        difftime_predicted = filtered_state_means

        # (smoothed_state_means, smoothed_state_covariances) = kf.smooth(measurements)
    return difftime_predicted  


if __name__ == "__main__":
    # main method usage    
    """
    Method: predict_list(line, direction, dayofweek, period, weather,stop_list=None, model=0):
    Input
        line: routeid; direction: 1 or 2; stop_list: list of stopids
        dayofweek [0:6]; period: '05:00:00'-'00:00:00'; weather: 'Fair' or 'Bad'
        model(int): from 0 to ...
        0: Linear_SVM
        1: SVM
        2: Avarage_model
    
    Output
        result_cum
    """
    print(predict_list(13, 1, 1, '8:30:00', 'Fair',stop_list=[2143,2145,4670], model=0))
    # if stop_list missed or is None, choose whole route of the frist trip.
    print(predict_list(13, 1, 1, '8:30:00', 'Fair', model=2))
