from transformer import *
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
import MySQLdb
import datetime
import joblib


def access_mysql(cur, line, direction):
    # cur.execute('select * from busduck.leavetimes_01 LIMIT 0,10;')
    query = """
    SELECT * FROM busduck.rt_leavetimes_db where TRIPID in 
    (SELECT TRIPID FROM busduck.rt_trips_db where LINEID="{}" and DIRECTION = {});
    """
    cur.execute(query.format(line, direction))
    rows = cur.fetchall()
    return  pd.DataFrame(rows, columns=[i[0] for i in cur.description])

def save_pre_data(line, direction):
    cxn = MySQLdb.connect(user='user', password='nUT8+~nYRS/9-i$') # TODO change password loc
    cur = cxn.cursor()
    # Data base and Load weather
    DF = access_mysql(cur, line, direction)
    pipeline = Pipeline([
                        ('init',InitABT(line)),
                        ('fitering',Filter()),
                        ('dropcols',Dropunused())])
    ## OR 
    # init = InitABT(line)
    # y = init.transform(DF)

    # filter_1 = Filter()
    # y = filter_1.transform(y)

    # filter_2 = Dropunused()
    # y = filter_2.transform(y)
    y = pipeline.transform(DF)
    pkl_name = str(line) + "_" + str(direction) + ".pkl"
    joblib.dump(y, pkl_name)
    cur.close()

if __name__ == '__main__':
    # cxn = MySQLdb.connect(user='user', password='nUT8+~nYRS/9-i$') # TODO change password loc
    # cur = cxn.cursor()
    # cur.execute("SELECT distinct LINEID FROM busduck.rt_trips_db;")
    # all_routes = cur.fetchall()
    # cur.close()
    routes = ['104','11','111','116', '120', '122', '13']
    for i in routes:
        save_pre_data(i, 1)
        save_pre_data(i, 2)