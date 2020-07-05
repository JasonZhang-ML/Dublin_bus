import requests
# import MySQLdb # one method to connect to mysql, not sure use which one

# import sys
# import os
# sys.path.append(os.getcwd()+'\\src\\Externel_Data_API')

import url_keys
import logger

 
class BusWeatherCrawler:
    db_name = url_keys.DB_NAME

    # Real time bus infromation
    rtbi_api_url = url_keys.RTBI_API_URL
    # Time table bus information
    ttbi_api_url = url_keys.TTBI_API_URL
    # Bus stop Information
    bsi_api_url = url_keys.BSI_API_URL
    # Weather Information
    weather_api_url = url_keys.OW_API_URL
    weather_api_key_dict = url_keys.OW_API_KEY_DICT
    # Route Information
    route_api_url = url_keys.ROUTE_API_URL
    # Distance Information
    distance_api_url = url_keys.DISTANCE_API_URL

    LOGGER_NAME = 'weatherCrawlerLogger'

    def __init__(self):
        self.data = []
        self.log = logger.Logger(BusWeatherCrawler.LOGGER_NAME)

    def request_weather_api(self, lat, lng):
        url = BusWeatherCrawler.weather_api_url.format(
            lat=lat,
            lon=lng,
            key=url_keys.OW_API_KEY_DICT[0] # can change key
            )
        try:
            r = requests.get(url)
            self.log.INFO("request ow api: {}".format(url))
            
            if r.status_code != 200 or r.json() == None:
                self.log.WARN("request ow api failed: {}".format(r.status_code))
            
            ret = r.json()
            self.log.INFO("response: 200 OK")
            return ret
        except Exception as e:
            self.log.ERROR("request - {}: {}".format(url, e))



    def request_realtimebus_api(self, stopid, routeid=None):
        url = BusWeatherCrawler.rtbi_api_url.format(
            stopid=stopid,
            routeid= routeid if (routeid != None)  else ''
        )
        try:
            r = requests.get(url)
            self.log.INFO("request rtbi api: {}".format(url))

            if r.status_code != 200 or r.json() == None:
                self.log.WARN("request rtbi api failed: {}".format(r.status_code))

            ret = r.json()
            self.log.INFO("response: 200 OK")
            return ret
        except Exception as e:
            self.log.ERROR("request - {}: {}".format(url, e))


    def request_timetablebus_api(self, stopid, routeid):
        url = BusWeatherCrawler.ttbi_api_url.format(
            stopid=stopid,
            routeid=routeid
        )
        try:
            r = requests.get(url)
            self.log.INFO("request ttbi api: {}".format(url))

            if r.status_code != 200 or r.json() == None:
                self.log.WARN("request ttbi api failed: {}".format(r.status_code))

            ret = r.json()
            self.log.INFO("response: 200 OK")
            return ret
        except Exception as e:
            self.log.ERROR("request - {}: {}".format(url, e))

    def request_busstopinfo_api(self, stopid):
        url = BusWeatherCrawler.bsi_api_url.format(
            stopid=stopid
        )
        try:
            r = requests.get(url)
            self.log.INFO("request bsi api: {}".format(url))

            if r.status_code != 200 or r.json() == None:
                self.log.WARN("request bsi api failed: {}".format(r.status_code))

            ret = r.json()
            self.log.INFO("response: 200 OK")
            return ret
        except Exception as e:
            self.log.ERROR("request - {}: {}".format(url, e))


    def request_route_api_coor(self, orginLat, orginLon, destinationLat, destinationLon):
        url = BusWeatherCrawler.route_api_url.format(
            orgin = orginLat + "," + orginLon,
            destination = destinationLat + "," + destinationLon
        )
        try:
            r = requests.get(url)
            self.log.INFO("request route api: {}".format(url))

            if r.status_code != 200 or r.json() == None:
                self.log.WARN("request route api failed: {}".format(r.status_code))

            ret = r.json()
            self.log.INFO("response: 200 OK")
            return ret
        except Exception as e:
            self.log.ERROR("request - {}: {}".format(url, e))

    def request_route_api(self, orginid, destinationid):
        orgin = self.request_busstopinfo_api(orginid)
        destination = self.request_busstopinfo_api(destinationid)
        oLat = orgin['results'][0]['latitude']
        oLon = orgin['results'][0]['longitude']
        dLat = destination['results'][0]['latitude']
        dLon = destination['results'][0]['longitude']
        return self.request_route_api_coor(oLat, oLon, dLat, dLon)

    def request_distance_api(self, orginid, destinationid, routeid):
        orgin = self.request_busstopinfo_api(orginid)
        destination = self.request_busstopinfo_api(destinationid)
        oLat = orgin['results'][0]['latitude']
        oLon = orgin['results'][0]['longitude']
        dLat = destination['results'][0]['latitude']
        dLon = destination['results'][0]['longitude']
        url = BusWeatherCrawler.distance_api_url.format(
            orgin = oLat + "," + oLon,
            destination = dLat + "," + dLon
        )
        try:
            r = requests.get(url)
            self.log.INFO("request route api: {}".format(url))

            if r.status_code != 200 or r.json() == None:
                self.log.WARN("request route api failed: {}".format(r.status_code))

            ret = r.json()
            self.log.INFO("response: 200 OK")
            return int(ret['rows'][0]['elements'][0]['distance']['value'])
        except Exception as e:
            self.log.ERROR("request - {}: {}".format(url, e))



    def insert_weather_data(self, value_lst):
        # sql = """
        #     INSERT INTO {tb_name}
        #     (station_id, bike_stands, ava_bikes, ava_stands, status, last_update_jcd,
        #     weather_id,temp, feels_like,temp_min, temp_max, pressure, humidity, wind_speed, wind_deg, clouds, rain_1h,
        #     rain_3h, snow_1h, snow_3h, last_update_ow)
        #     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        #     """.format(tb_name=BusWeatherCrawler.weather_table)
        # ret = self.executemany(sql, value_lst) # depends
        # if not ret:
        #     self.log.WARN('insert weather failed')
        # else:
        #     self.log.INFO('insert weather success')
        pass

    def insert_realtimebus_data(self, value_lst):
        # sql = """ """
        # ret = self.db.executemany(sql, value_lst)
        # if not ret:
        #     self.log.WARN('')
        # else:
        #     self.log.INFO('')
        pass

    def insert_timetablebus_data(self, value_lst):
        # sql = """ """
        # ret = self.db.executemany(sql, value_lst)
        # if not ret:
        #     self.log.WARN('')
        # else:
        #     self.log.INFO('')
        pass

    def insert_busstopinfo_data(self, value_lst):
        # sql = """ """
        # ret = self.db.executemany(sql, value_lst)
        # if not ret:
        #     self.log.WARN('')
        # else:
        #     self.log.INFO('')
        pass

    def worker(self):
        pass

if __name__ == "__main__":

    ## one method to connect to mysql, not sure use which one
    # Connect to mysql
    # cxn = MySQLdb.connect()
    # cur = cxn.cursor()

    crawler = BusWeatherCrawler()

    # get weather
    #print(crawler.request_weather_api(5.349562, -7.278198))
    # realtimebus can be request without routeid
    #print(crawler.request_realtimebus_api(46))
    #print(crawler.request_realtimebus_api(46,16))
    # time table
    #print(crawler.request_timetablebus_api(46,16))
    # stop info
    #print(crawler.request_busstopinfo_api(46))
    # route info
    #print(crawler.request_route_api(1380,1381))
    #distance info
    print(crawler.request_distance_api(1380, 1381, str(17)))
    # crawler.worker()