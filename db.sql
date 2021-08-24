-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        10.6.4-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- pythondb 데이터베이스 구조 내보내기
CREATE DATABASE IF NOT EXISTS `pythondb` /*!40100 DEFAULT CHARACTER SET utf8mb3 */;
USE `pythondb`;

-- 테이블 pythondb.tbl_keyword 구조 내보내기
CREATE TABLE IF NOT EXISTS `tbl_keyword` (
  `keyword` varchar(50) NOT NULL,
  PRIMARY KEY (`keyword`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- 테이블 데이터 pythondb.tbl_keyword:~3 rows (대략적) 내보내기
DELETE FROM `tbl_keyword`;
/*!40000 ALTER TABLE `tbl_keyword` DISABLE KEYS */;
INSERT INTO `tbl_keyword` (`keyword`) VALUES
	('로마'),
	('바르셀로나'),
	('파리');
/*!40000 ALTER TABLE `tbl_keyword` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
tbl_crawlingdatatbl_keyword