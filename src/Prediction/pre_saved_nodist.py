from transformer import *
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
import pymysql
import joblib
import os


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
    cxn = pymysql.connect(user='user', password='nUT8+~nYRS/9-i$') # TODO change password loc
    cur = cxn.cursor()
    # Data base and Load weather
    DF = access_mysql(cur, line, direction)
    pipeline = Pipeline([
                        ('init',InitABT_nodist(line)),
                        ('fitering',Filter_nodist())])
    ## OR 
    # init = InitABT(line)
    # y = init.transform(DF)

    # filter_1 = Filter()
    # y = filter_1.transform(y)

    # filter_2 = Dropunused()
    # y = filter_2.transform(y)
    y = pipeline.transform(DF)
    pkl_name = str(line) + "_" + str(direction) + "_n.pkl" # means No distance
    joblib.dump(y, pkl_name)
    cur.close()

if __name__ == '__main__':
    # routes = ['104','11','111','116', '120', '122', '13']
    cxn = pymysql.connect(user='root', password='kki880611') # TODO change password loc
    cur = cxn.cursor()
    cur.execute("SELECT distinct LINEID FROM busduck.rt_trips_db;")
    all_routes = cur.fetchall()
    cur.close()
    all_routes = [list(item) for item in all_routes]
    all_routes = sum(all_routes, [])
    all_routes.reverse()
    routes = all_routes

    for i in routes:
        try:
            pkl_name = str(i) + "_" + str(1) + "_n.pkl"
            if ~os.path.exists(pkl_name):
                save_pre_data(i, 1)
        except Exception:
            pass
        try:
            pkl_name = str(i) + "_" + str(2) + "_n.pkl"
            if ~os.path.exists(pkl_name):
                save_pre_data(i, 2)
        except Exception:
            pass
        continue