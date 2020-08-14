import sys
sys.path.append('../../src')
#from Externel_Data_API.bus_weather_crawler import BusWeatherCrawler
from Prediction.load_predict_nodist import predict_every_two
import joblib
import numpy as np
import os
import json



def getWeather():
    crawler = BusWeatherCrawler()
    result = crawler.request_weather_api(53.2989008333,-6.1959722222)
    #rDict = {"main": result['weather'][0]['main'], "temp": result['main']['temp']}
    #j = json.dump(rDict)
    return result['weather'][0]['main']

def loadModel(dirc ,route_id):
    pkl_name = str(route_id) +"_" + str(dirc) + "_n.pkl"
    if os.path.exists(pkl_name):
        DF = joblib.load(pkl_name)
        return DF
    return None

def getRouteStops(route_id, ori, des):
    stops_file = open('route_stops.json', 'r')
    stops_dic = json.load(stops_file)
    route_id_1 = route_id + '_1'
    route_id_2 = route_id + '_2'

    oriFind = False
    desFind = False
    for i in stops_dic[route_id_1]:
        if(i == ori):
            oriFind = True
        if(oriFind and i == des):
            desFind = True
            break
    
    if(oriFind and desFind):
        result = []
        enterInternal = False
        for i in stops_dic[route_id_1]:
            if(enterInternal or i == ori):
                result.append(i)
                enterInternal = True
            if(i == des):
                break
        result.append(1)
        return result


    oriFind = False
    desFind = False
    for i in stops_dic[route_id_2]:
        if(i == ori):
            oriFind = True
        if(oriFind and i == des):
            desFind = True
            break
    
    if(oriFind and desFind):
        result = []
        enterInternal = False
        for i in stops_dic[route_id_2]:
            if(enterInternal or i == ori):
                result.append(i)
                enterInternal = True
            if(i == des):
                break
        result.append(2)
        return result

    return []
    
        


def getPredict(route_id, ori_id, des_id, dayofweek, time):
    try:
        model = None
        stops = []


        stops = getRouteStops(route_id, ori_id, des_id)
        if(stops == []):
            return -1

        direction = stops[-1]
        stops.pop()
        
        model = loadModel(direction, route_id)
        if(model is None):
            return -1
        
        

        predictTime = ""
        if(int(time[3]) >= 3):
            predictTime = time[0: 3] + "30:00"
        else:
            predictTime = time[0: 3] + "00:00"


        #weather = getWeather()
        weather = 'Fair'

        results = 0
        for i in range(0, len(stops) - 1):
            time = predict_every_two(stops[i], stops[i + 1], dayofweek, predictTime, weather, model, 0)
            if(type(time[0]) == np.float64 or type(time[0]) == int):
                results += float(time[0])
        return results
    except Exception:
        return -1

    
if __name__ == '__main__':
    print(getPredict('44', '2818', '2825', 0, '08:00:00'))
