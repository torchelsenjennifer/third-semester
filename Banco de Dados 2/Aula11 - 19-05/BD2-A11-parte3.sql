DROP DATABASE IF EXISTS aula11;
CREATE DATABASE IF NOT EXISTS aula11;
USE aula11;

CREATE TABLE t1(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	valor INT NOT NULL
) ENGINE=MyISAM;
CREATE INDEX idx_t1valor ON t1(valor);

create TABLE t2(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	valor INT NOT NULL
) ENGINE=MyISAM;
 
CREATE TABLE t3(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    valor INT NOT NULL
) ENGINE=INNODB;
CREATE INDEX idx_t3valor ON t3(valor);
 
create TABLE t4(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    valor INT NOT NULL
) ENGINE=INNODB;

DELIMITER $$
CREATE PROCEDURE inseret1(IN qtdLinhas INT, IN minVal INT, IN maxVal INT)
    BEGIN
        DECLARE i INT;
        DECLARE tmp INT;
        SET i = 1;
        START TRANSACTION;
        WHILE i <= qtdLinhas DO
            SET tmp = minVal + CEIL(RAND() * (maxVal - minVal)); 
            -- CEIL ou CEILING -> arredonda para cima
            INSERT INTO t1 (valor) VALUES (tmp);
            SET i = i + 1;
        END WHILE;
        COMMIT;
    END$$
DELIMITER ;


DELIMITER $$
CREATE PROCEDURE inseret2(IN qtdLinhas INT, IN minVal INT, IN maxVal INT)
    BEGIN
        DECLARE i INT;
        DECLARE tmp INT;
        SET i = 1;
        START TRANSACTION;
        WHILE i <= qtdLinhas DO
            SET tmp = minVal + CEIL(RAND() * (maxVal - minVal)); 
            -- CEIL ou CEILING -> arredonda para cima
            INSERT INTO t2 (valor) VALUES (tmp);
            SET i = i + 1;
        END WHILE;
        COMMIT;
    END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE inseret3(IN qtdLinhas INT, IN minVal INT, IN maxVal INT)
    BEGIN
        DECLARE i INT;
        DECLARE tmp INT;
        SET i = 1;
        START TRANSACTION;
        WHILE i <= qtdLinhas DO
            SET tmp = minVal + CEIL(RAND() * (maxVal - minVal)); 
            -- CEIL ou CEILING -> arredonda para cima
            INSERT INTO t3 (valor) VALUES (tmp);
            SET i = i + 1;
        END WHILE;
        COMMIT;
    END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE inseret4(IN qtdLinhas INT, IN minVal INT, IN maxVal INT)
    BEGIN
        DECLARE i INT;
        DECLARE tmp INT;
        SET i = 1;
        START TRANSACTION;
        WHILE i <= qtdLinhas DO
            SET tmp = minVal + CEIL(RAND() * (maxVal - minVal)); 
            -- CEIL ou CEILING -> arredonda para cima
            INSERT INTO t4 (valor) VALUES (tmp);
            SET i = i + 1;
        END WHILE;
        COMMIT;
    END$$
DELIMITER ;

CALL inseret1(50000, 850, 99999);
CALL inseret2(50000, 850, 99999);
CALL inseret3(50000, 850, 99999);
CALL inseret4(50000, 850, 99999);

SELECT SQL_NO_CACHE valor
FROM t1 
WHERE valor > 900 AND valor < 950
ORDER BY valor;

SELECT SQL_NO_CACHE valor
FROM t2 
WHERE valor > 900 AND valor < 950
ORDER BY valor;

SELECT SQL_NO_CACHE valor
FROM t3 
WHERE valor > 900 AND valor < 950
ORDER BY valor;

SELECT SQL_NO_CACHE valor
FROM t4 
WHERE valor > 900 AND valor < 950
ORDER BY valor;

