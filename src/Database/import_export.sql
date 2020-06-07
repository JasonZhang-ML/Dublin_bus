-- Import -- 
load data local infile "~/data/rt_vehicles_DB_2018.txt" into table `rt_vehicles_db`
fields terminated by ';'  
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(DATASOURCE, @DAYOFSERVICE, VEHICLEID, DISTANCE, MINUTES, @LASTUPDATE, NOTE)
set DAYOFSERVICE = str_to_date(@DAYOFSERVICE, '%d-%M-%Y %H:%i:%s'),
LASTUPDATE = str_to_date(@LASTUPDATE, '%d-%M-%Y %H:%i:%s');

load data local infile "~/data/rt_trips_DB_2018.txt" into table `rt_trips_db`
fields terminated by ';'  
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(DATASOURCE, @DAYOFSERVICE, TRIPID, LINEID, ROUTEID, DIRECTION, PLANNEDTIME_ARR, PLANNEDTIME_DEP, ACTUALTIME_ARR, ACTUALTIME_DEP, BASIN, TENDERLOT, SUPPRESSED, JUSTIFICATIONID, @LASTUPDATE, NOTE)
set DAYOFSERVICE = str_to_date(@DAYOFSERVICE, '%d-%M-%Y %H:%i:%s'),
LASTUPDATE = str_to_date(@LASTUPDATE, '%d-%M-%Y %H:%i:%s');

load data local infile "~/data/rt_leavetimes_DB_2018.txt" into table `rt_leavetimes_db`
fields terminated by ';'  
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(DATASOURCE, @DAYOFSERVICE, TRIPID, PROGRNUMBER, STOPPOINTID, PLANNEDTIME_ARR, PLANNEDTIME_DEP, ACTUALTIME_ARR, ACTUALTIME_DEP, VEHICLEID, PASSENGERS, PASSENGERSIN, PASSENGERSOUT, DISTANCE, SUPPRESSED, JUSTIFICATIONID, @LASTUPDATE, NOTE)
set DAYOFSERVICE = str_to_date(@DAYOFSERVICE, '%d-%M-%Y %H:%i:%s'),
LASTUPDATE = str_to_date(@LASTUPDATE, '%d-%M-%Y %H:%i:%s');


-- Export -- 
SELECT DATASOURCE, DAYOFSERVICE, VEHICLEID, DISTANCE, MINUTES, LASTUPDATE FROM `rt_vehicles_db` WHERE month(DAYOFSERVICE) = 1
INTO OUTFILE 'D:/datasets/Dublin_bus/01/rt_vehicles_db_01.csv'
fields terminated by ';'  
LINES TERMINATED BY '\r\n';

SELECT DATASOURCE, DAYOFSERVICE, TRIPID, LINEID, ROUTEID, DIRECTION, PLANNEDTIME_ARR, PLANNEDTIME_DEP, ACTUALTIME_ARR, ACTUALTIME_DEP, LASTUPDATE FROM `rt_trips_db` WHERE month(DAYOFSERVICE) = 1
INTO OUTFILE 'D:/datasets/Dublin_bus/01/rt_trips_db_01.csv'
fields terminated by ';'  
LINES TERMINATED BY '\r\n';

SELECT DATASOURCE, DAYOFSERVICE, TRIPID, PROGRNUMBER, STOPPOINTID, PLANNEDTIME_ARR, PLANNEDTIME_DEP, ACTUALTIME_ARR, ACTUALTIME_DEP, VEHICLEID,  LASTUPDATE FROM `rt_leavetimes_db` WHERE month(DAYOFSERVICE) = 1
INTO OUTFILE 'D:/datasets/Dublin_bus/01/rt_leavetimes_db_01.csv'
fields terminated by ';'  
LINES TERMINATED BY '\r\n';

-- SELECT @@sql_mode;
-- SHOW VARIABLES;

-- SELECT str_to_date('23-NOV-18 00:00:00', '%d-%M-%Y %H:%i:%s');

    
    
    