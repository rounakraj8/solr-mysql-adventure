CREATE TABLE `user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `country` text,
  `dob` date DEFAULT NULL,
  `first_name` text,
  `job` text,
  `last_name` text,
  `last_modified` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1;
