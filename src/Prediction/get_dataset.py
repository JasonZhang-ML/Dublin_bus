from transformer import *
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
import MySQLdb
import datetime

if __name__ == '__main__':
    line = "17"
    direction = 1
    # Data base and Load weather
    cxn = MySQLdb.connect(user='user', password='nUT8+~nYRS/9-i$')
    cur = cxn.cursor()


    def GetData(cur, line, direction):
        # cur.execute('select * from busduck.leavetimes_01 LIMIT 0,10;')
        query = """
        SELECT * FROM busduck.rt_leavetimes_db where TRIPID in 
        (SELECT TRIPID FROM busduck.rt_trips_db where LINEID="{}" and DIRECTION = {});
        """
        cur.execute(query.format(line, direction))
        rows = cur.fetchall()
        return  pd.DataFrame(rows, columns=[i[0] for i in cur.description])

    DF = GetData(cur, line, direction)
    init = InitABT(line)
    y = init.transform(DF)
    print(y.head())
    y
    # pipeline = Pipeline([
    #                     ('init',InitABT(line)),
    #                     ('fitering',Filter())])
    # p = pipeline.fit(DF)
    # print(p)
    