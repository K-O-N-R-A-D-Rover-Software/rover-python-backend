CREATE SCHEMA `rover`;

CREATE TABLE `rover`.`measurement` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `timestamp` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `pressureInhPa` FLOAT NOT NULL,
  `tempInC` FLOAT NOT NULL,
  `magnetFieldInGauss` FLOAT NOT NULL,
  `gyroscopeInDPS` FLOAT NOT NULL,
  `accellerationInG` FLOAT NOT NULL,
  PRIMARY KEY (`id`));
  
/* Beispielwerte */
insert into measurement (pressureInhPa, tempInC, magnetFieldInGauss, gyroscopeInDPS, accellerationInG) values (1024, 13.4, 4.15, 3.65, 0.75);
insert into measurement (pressureInhPa, tempInC, magnetFieldInGauss, gyroscopeInDPS, accellerationInG) values (1021, 13.5, 4.13, -1.65, 1.75);