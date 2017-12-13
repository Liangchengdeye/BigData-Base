# Host: localhost  (Version: 5.5.53)
# Date: 2017-12-13 10:37:51
# Generator: MySQL-Front 5.3  (Build 4.234)

/*!40101 SET NAMES utf8 */;

#
# Structure for table "test01"
#

DROP TABLE IF EXISTS `test01`;
CREATE TABLE `test01` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

#
# Data for table "test01"
#

/*!40000 ALTER TABLE `test01` DISABLE KEYS */;
INSERT INTO `test01` VALUES (1,'1001'),(2,'1002'),(3,'1003'),(4,'1004'),(5,'1005'),(6,'1006');
/*!40000 ALTER TABLE `test01` ENABLE KEYS */;

#
# Structure for table "test02"
#

DROP TABLE IF EXISTS `test02`;
CREATE TABLE `test02` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

#
# Data for table "test02"
#

/*!40000 ALTER TABLE `test02` DISABLE KEYS */;
INSERT INTO `test02` VALUES (1,'01'),(2,'02'),(3,'03'),(4,'04'),(5,'05'),(6,'06');
/*!40000 ALTER TABLE `test02` ENABLE KEYS */;
