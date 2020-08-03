SELECT stop_id, stop_name FROM stops WHERE stop_id IN (
	SELECT DISTINCT stop_id FROM stop_times WHERE trip_id IN (
		SELECT trip_id FROM trips WHERE route_id = <route_id>));