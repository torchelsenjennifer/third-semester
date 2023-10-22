SET autocommit = 0; -- Desabilitando o autocommit
SET autocommit = 1; -- Habilita o autocommit

DROP DATABASE IF EXISTS aula12;
CREATE DATABASE aula12;
USE aula12;

-- ATOR
CREATE TABLE ator (
  id INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(45) NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO ator (nome) VALUES('Adam Sandler');
INSERT INTO ator (nome) VALUES('Hey Decio');
INSERT INTO ator (nome) VALUES('Jamie Foxx');
INSERT INTO ator (nome) VALUES('Joaquim Phoenix');
INSERT INTO ator (nome) VALUES('Jude Law');
INSERT INTO ator (nome) VALUES('Meryl Streep');
INSERT INTO ator (nome) VALUES('Michael Douglas');
INSERT INTO ator (nome) VALUES('Tom Cruise');