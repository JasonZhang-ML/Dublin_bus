import sys
sys.path.append('../../src')
sys.path.append('./src')
import json
from Prediction.load_predict_nodist import predict_list
from Externel_Data_API.bus_weather_crawler import BusWeatherCrawler


def GetRouteStops(start, end, routeid):
    stops_file = open('./route_stops.json', 'r')
    stops_dic = json.load(stops_file)
    route_id_1 = routeid + '_1'
    route_id_2 = routeid + '_2'

    try:
        route = stops_dic[route_id_1]
        start_ix = route.index(start)
        end_ix = route.index(end)

        if start_ix <= end_ix:
            return [route[start_ix:end_ix+1], 1]
        else:
            print('not correct order in the list')
            # return [route[end_ix:start_ix+1], 1]
            return [None, None]
    except Exception as e:
        print(e)
        pass

    try:
        route = stops_dic[route_id_2]
        start_ix = route.index(start)
        end_ix = route.index(end)

        if start_ix <= end_ix:
            return [route[start_ix:end_ix+1], 2]
        else:
            print('not correct order in the list')
            # return [route[end_ix:start_ix+1], 2] # force output
            return [None, None]
    except Exception as e:
        pass



## Period
# period = ""
# if(int(time[3]) >= 3):
#     period = time[0: 3] + "30:00"
# else:
#     period = time[0: 3] + "00:00"

## weather
crawler = BusWeatherCrawler()
result = crawler.request_weather_api(53.2989008333,-6.1959722222)
if result['weather'][0]['main'] in ['Clear', 'Clouds','Drizzle']:
    weather = 'Fair'
else:
    weather = "Bad"

print(weather)

routeid = '14'
start = '0248'
end = '0250'
stop_l, direction = GetRouteStops(start,end,routeid)
print(direction)
print(stop_l)
if stop_l != None:
    # print(predict_list(routeid, direction, 1, '8:30:00', weather,stop_list=stop_l, model=0))
    print(predict_list(routeid, direction, 1, '8:30:00', weather,stop_list=None, model=2))