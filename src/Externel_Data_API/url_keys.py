# weather api url
OW_API_URL = "http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}&units=Metric"
# weather api key
OW_API_KEY_DICT = {
    0: "8f67620b4782d168bef1be242f719519",
    1: "3501df5f57129b4f18c31c7bebcac8d7",
    2: "ecd39e5a21a31b0fe97e9914d999bc9c", 
}

# Real time bus infromation
RTBI_API_URL = "https://data.smartdublin.ie/cgi-bin/rtpi/realtimebusinformation?stopid={stopid}&routeid={routeid}&format=json"

# Time table bus information
TTBI_API_URL = "https://data.smartdublin.ie/cgi-bin/rtpi/timetableinformation?type=week&stopid={stopid}&routeid={routeid}&format=json"

# Bus stop Information
BSI_API_URL = "https://data.smartdublin.ie/cgi-bin/rtpi/busstopinformation?stopid={stopid}&format=json"

# db
DB_SERVER = ""  # host name
DB_USER = ""  # user name
DB_PASSWORD = ""  # password
DB_PORT = 3306



# ONLINE
# DB_NAME = 'busduck'

# Test
DB_NAME = 'test'
