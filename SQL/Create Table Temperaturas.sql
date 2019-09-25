CREATE TABLE `Temperaturas` (
 `id` int(11) NOT NULL AUTO_INCREMENT,
 `horario` datetime NOT NULL,
 `temp1` float NOT NULL,
 `temp2` float DEFAULT NULL,
 `temp3` float DEFAULT NULL,
 `unidade` char(1) NOT NULL,
 PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=824 DEFAULT CHARSET=utf8mb4;
