CREATE DATABASE `busdata`;

USE `busdata`;

CREATE TABLE `routes` (
  `route_id` varchar(24) NOT NULL,
  `agency_id` varchar(10) NOT NULL,
  `route_short_name` varchar(24) NOT NULL,
  `route_long_name` varchar(30) DEFAULT NULL,
  `route_type` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`route_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ;


CREATE TABLE `trips` (
  `route_id` varchar(24) NOT NULL,
  `service_id` varchar(10) NOT NULL,
  `trip_id` varchar(30) NOT NULL,
  `shape_id` varchar(24) DEFAULT NULL,
  `trip_headsign` varchar(75) DEFAULT NULL,
  `direction_id` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`trip_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ;

CREATE TABLE `stop_times` (
  `trip_id` varchar(30) NOT NULL,
  `arrival_id` varchar(20) NOT NULL,
  `departure_time` varchar(24) NOT NULL,
  `stop_id` varchar(24) NOT NULL,
  `stop_sequence` varchar(45) DEFAULT NULL,
  `stop_headsign` varchar(24) DEFAULT NULL,
  `pickup_type` varchar(24) DEFAULT NULL,
  `drop_off_type` varchar(24) DEFAULT NULL,
  `shape_dist_traveled` varchar(24) DEFAULT NULL,
  PRIMARY KEY (`trip_id` , `stop_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ;

CREATE TABLE `stops` (
  `stop_id` varchar(24) NOT NULL,
  `stop_name` varchar(40) NOT NULL,
  `stop_lat` varchar(24) NOT NULL,
  `stop_lon` varchar(24) DEFAULT NULL,
  PRIMARY KEY (`stop_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ;