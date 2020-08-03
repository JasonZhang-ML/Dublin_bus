load data infile 'D:/ChromeDownload/11111/stops.txt'

into table busdata.stops

fields terminated by ',' optionally enclosed by '"' escaped by '"'

lines terminated by '\r\n';


load data infile 'D:/ChromeDownload/11111/stop_times.txt'

into table busdata.stop_times

fields terminated by ',' optionally enclosed by '"' escaped by '"'

lines terminated by '\r\n';


load data infile 'D:/ChromeDownload/11111/trips.txt'

into table busdata.trips

fields terminated by ',' optionally enclosed by '"' escaped by '"'

lines terminated by '\r\n';


load data infile 'D:/ChromeDownload/11111/routes.txt'

into table busdata.routes

fields terminated by ',' optionally enclosed by '"' escaped by '"'

lines terminated by '\r\n';
