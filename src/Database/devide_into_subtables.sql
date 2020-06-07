CREATE TABLE vehicles_01  SELECT * FROM rt_vehicles_db where  month(DAYOFSERVICE) = 1;
CREATE TABLE trips_01  SELECT * FROM rt_trips_db where  month(DAYOFSERVICE) = 1;
CREATE TABLE leavetimes_01  SELECT * FROM rt_leavetimes_db where  month(DAYOFSERVICE) = 1;