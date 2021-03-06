-- SQL used to created required tables;

CREATE DATABASE `busduck`;

USE `busduck`;

CREATE TABLE `rt_vehicles_db` (
  `DATASOURCE` varchar(4) NOT NULL,
  `DAYOFSERVICE` datetime NOT NULL,
  `VEHICLEID` varchar(7) NOT NULL,
  `DISTANCE` int(11) DEFAULT NULL,
  `MINUTES` int(11) DEFAULT NULL,
  `LASTUPDATE` datetime DEFAULT NULL,
  `NOTE` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`DATASOURCE`,`DAYOFSERVICE`,`VEHICLEID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ;

CREATE TABLE `rt_trips_db` (
  `DATASOURCE` varchar(4) NOT NULL,
  `DAYOFSERVICE` datetime NOT NULL,
  `TRIPID` varchar(30) NOT NULL,
  `LINEID` varchar(10) DEFAULT NULL,
  `ROUTEID` varchar(20) DEFAULT NULL,
  `DIRECTION` varchar(2) DEFAULT NULL,
  `PLANNEDTIME_ARR` int(11) DEFAULT NULL,
  `PLANNEDTIME_DEP` int(11) DEFAULT NULL,
  `ACTUALTIME_ARR` int(11) DEFAULT NULL,
  `ACTUALTIME_DEP` int(11) DEFAULT NULL,
  `BASIN` varchar(20) DEFAULT NULL,
  `TENDERLOT` int(11) DEFAULT NULL,
  `SUPPRESSED` int(11) DEFAULT NULL,
  `JUSTIFICATIONID` int(11) DEFAULT NULL,
  `LASTUPDATE` datetime DEFAULT NULL,
  `NOTE` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`DATASOURCE`,`DAYOFSERVICE`,`TRIPID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `rt_leavetimes_db` (
  `DATASOURCE` varchar(4) NOT NULL,
  `DAYOFSERVICE` datetime NOT NULL,
  `TRIPID` varchar(30) NOT NULL,
  `PROGRNUMBER` int(11) NOT NULL,
  `STOPPOINTID` varchar(16) DEFAULT NULL,
  `PLANNEDTIME_ARR` int(11) DEFAULT NULL,
  `PLANNEDTIME_DEP` int(11) DEFAULT NULL,
  `ACTUALTIME_ARR` int(11) DEFAULT NULL,
  `ACTUALTIME_DEP` int(11) DEFAULT NULL,
  `VEHICLEID` varchar(7) DEFAULT NULL,
  `PASSENGERS` int(11) DEFAULT NULL,
  `PASSENGERSIN` int(11) DEFAULT NULL,
  `PASSENGERSOUT` int(11) DEFAULT NULL,
  `DISTANCE` int(11) DEFAULT NULL,
  `SUPPRESSED` int(11) DEFAULT NULL,
  `JUSTIFICATIONID` int(11) DEFAULT NULL,
  `LASTUPDATE` datetime DEFAULT NULL,
  `NOTE` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`DATASOURCE`,`DAYOFSERVICE`,`TRIPID`,`PROGRNUMBER`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- ALTER  TABLE 表名 CHANGE [column] 旧字段名 新字段名 新数据类型;
-- alter  table table1 change column1 column1 varchar(100) DEFAULT 1.2 COMMENT '注释'; -- 正常，此时字段名称没有改变，能修改字段类型、类型长度、默认值、注释
-- alter  table table1 change column1 column2 decimal(10,1) DEFAULT NULL COMMENT '注释' -- 正常，能修改字段名、字段类型、类型长度、默认值、注释
-- alter  table table1 change column2 column1 decimal(10,1) DEFAULT NULL COMMENT '注释' -- 正常，能修改字段名、字段类型、类型长度、默认值、注释
ALTER
