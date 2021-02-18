CREATE DATABASE `cadence_test` /*!40100 DEFAULT CHARACTER SET latin1 */;


-- cadence_test.cpu_usage definition

CREATE TABLE `cpu_usage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cpu` varchar(100) COLLATE latin1_bin NOT NULL,
  `value_percent` varchar(100) COLLATE latin1_bin NOT NULL,
  `ref_time_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cpu_usage_FK_1` (`ref_time_id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=latin1 COLLATE=latin1_bin;


-- cadence_test.machine definition

CREATE TABLE `machine` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE latin1_bin NOT NULL,
  `ip` varchar(100) COLLATE latin1_bin NOT NULL,
  `create_in` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `hostname` varchar(100) COLLATE latin1_bin NOT NULL,
  `username` varchar(100) COLLATE latin1_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1 COLLATE=latin1_bin;


-- cadence_test.mem_usage definition

CREATE TABLE `mem_usage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mem_usage_percent` double DEFAULT NULL,
  `ref_time_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1 COLLATE=latin1_bin;


-- cadence_test.connection_active definition

CREATE TABLE `connection_active` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `connected` varchar(100) COLLATE latin1_bin NOT NULL,
  `ref_time_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1 COLLATE=latin1_bin;


-- cadence_test.ref_time definition

CREATE TABLE `ref_time` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time_ref` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `machine_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ref_time_FK` (`machine_id`),
  CONSTRAINT `ref_time_FK` FOREIGN KEY (`machine_id`) REFERENCES `machine` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=latin1 COLLATE=latin1_bin;


-- cadence_test.users_connected definition

CREATE TABLE `users_connected` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` varchar(100) COLLATE latin1_bin NOT NULL,
  `tty` varchar(100) COLLATE latin1_bin NOT NULL,
  `time` varchar(100) COLLATE latin1_bin NOT NULL,
  `from_s` varchar(100) COLLATE latin1_bin NOT NULL,
  `ref_time_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `users_connected_FK` (`ref_time_id`),
  CONSTRAINT `users_connected_FK` FOREIGN KEY (`ref_time_id`) REFERENCES `ref_time` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1 COLLATE=latin1_bin;


-- cadence_test.disk_usage definition

CREATE TABLE `disk_usage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `filesystem` varchar(100) COLLATE latin1_bin DEFAULT NULL,
  `type` varchar(100) COLLATE latin1_bin DEFAULT NULL,
  `size` varchar(100) COLLATE latin1_bin DEFAULT NULL,
  `used` varchar(100) COLLATE latin1_bin DEFAULT NULL,
  `mounted_on` varchar(100) COLLATE latin1_bin DEFAULT NULL,
  `available` varchar(100) COLLATE latin1_bin DEFAULT NULL,
  `use_percent` double DEFAULT NULL,
  `ref_time_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `disk_usage_FK` (`ref_time_id`),
  CONSTRAINT `disk_usage_FK` FOREIGN KEY (`ref_time_id`) REFERENCES `ref_time` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=270 DEFAULT CHARSET=latin1 COLLATE=latin1_bin;


-- cadence_test.proccess_running definition

CREATE TABLE `proccess_running` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` varchar(100) COLLATE latin1_bin DEFAULT NULL,
  `pid` varchar(100) COLLATE latin1_bin DEFAULT NULL,
  `vsz` varchar(100) COLLATE latin1_bin DEFAULT NULL,
  `rss` varchar(100) COLLATE latin1_bin DEFAULT NULL,
  `tty` varchar(100) COLLATE latin1_bin DEFAULT NULL,
  `stat` varchar(100) COLLATE latin1_bin DEFAULT NULL,
  `start` varchar(100) COLLATE latin1_bin DEFAULT NULL,
  `time` varchar(100) COLLATE latin1_bin DEFAULT NULL,
  `command` varchar(800) COLLATE latin1_bin DEFAULT NULL,
  `cpu_percent` varchar(100) COLLATE latin1_bin DEFAULT NULL,
  `men_percent` varchar(100) COLLATE latin1_bin DEFAULT NULL,
  `ref_time_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `proccess_running_FK` (`ref_time_id`),
  CONSTRAINT `proccess_running_FK` FOREIGN KEY (`ref_time_id`) REFERENCES `ref_time` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1326 DEFAULT CHARSET=latin1 COLLATE=latin1_bin;