import pymysql
from sqlalchemy import create_engine


def connect_db(localhost = "127.0.0.1", user = "root", password = "Ucd-cd-2019!", databasename = "busduck", port = "3306"):
    ''' Function to connect to the database '''
    try:
        return create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(user, password, localhost, port, databasename), echo=False)
    except Exception as e:
        print("Error: ", e)


def get_line_ids():
    engine = connect_db()
    sql = "SELECT DISTINCT LINEID FROM busduck.rt_trips_db ORDER BY LINEID;"
    rows = engine.execute(sql).fetchall()
    engine.dispose()
    return rows

def get_trip_ids():
    engine = connect_db()
    sql = "SELECT DISTINCT TRIPID FROM busduck.rt_trips_db ORDER BY TRIPID;"
    rows = engine.execute(sql).fetchall()
    engine.dispose()
    return rows

if(__name__ == "__main__"):
    print(get_line_ids())
    print(get_trip_ids())


