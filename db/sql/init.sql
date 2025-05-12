CREATE DATABASE IF NOT EXISTS `examproctordb`
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE `examproctordb`;

DROP TABLE IF EXISTS `students`;

CREATE TABLE `students` (
  `ID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(255) NOT NULL,
  `Email` VARCHAR(255) NOT NULL,
  `Password` VARCHAR(255) NOT NULL,
  `Role` ENUM('STUDENT','ADMIN') NOT NULL DEFAULT 'STUDENT',
  PRIMARY KEY (`ID`),
  UNIQUE KEY `uq_students_email` (`Email`)
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;
