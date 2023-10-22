DROP DATABASE IF EXIST AULA03;
CREATE DATABASE IF NOT EXISTS AULA03;
USE AULA03;

DROP TABLE IS EXIST empregado;
CREATE TABLE IF NOT EXISTS empregado(
    codigo INT,
    nome CHAR(40) NOT NULL,
    setor CHAR(2),
    cargo CHAR(20),
    salario decimal(10,2),
    PRIMARY KEY(codigo)
);

INSERT INTO empregado VALUES (1,"Edecio Muito Legal","2","Designer",1000);
INSERT INTO empregado VALUES (3,"Eduardo Monks","5","Dev",1500);
INSERT INTO empregado VALUES (4,"Raquel Murillo","4","Dev",1500);
INSERT INTO empregado VALUES (6,"Gladimau Catarino","4","Analista", 2200);
INSERT INTO empregado VALUES (7,"Sergio Marquina","4","Boss",9900 );
INSERT INTO empregado VALUES (9,"Alicia Sierra","5","Boss", 9900 );
INSERT INTO empregado VALUES (10,"Angelo Light","1","Dev",1500);
INSERT INTO empregado VALUES (15,"Silene Oliveira","1","DBA",2500 );
INSERT INTO empregado VALUES (25,"Darta Inhame","3","Designer",1650 );

SELECT * FROM empregado;

SELECT codigo, nome FROM empregado;

SELECT * FROM empregado WHERE (nome = "Sergio Marquina");

UPDATE empregado SET nome = "Salvador Martin" WHERE nome = "Sergio Marquina";

SELECT * FROM empregado;

DELETE FROM empregado WHERE setor = "3";

SELECT * FROM empregado WHERE (setor = "1") ORDER BY cargo;

SELECT * FROM empregado ORDER BY cargo DESC, nome ASC;


==========================================================================================================

# EXERCICIO 1 AULA03

#EXERCICIO 01 =============================================================================================

SELECT * FROM empregado;

#EXERCICIO 02 ==============================================================================================

SELECT nome, cargo FROM empregado;

#EXERCICIO 03 ==============================================================================================

SELECT * FROM empregado WHERE (setor = "1");

#EXERCICIO 04 ==============================================================================================

SELECT nome, salario FROM empregado ORDER BY nome ASC;

#EXERCICIO 05 ==============================================================================================

SELECT nome, salario FROM empregado ORDER BY nome DESC;

#EXERCICIO 06 ==============================================================================================

SELECT setor, nome FROM empregado ORDER BY setor ASC, nome DESC;

#EXERCICIO 07 ==============================================================================================

SELECT nome FROM empregado WHERE setor ="4" ORDER BY nome;

#EXERCICIO 08 ==============================================================================================

UPDATE empregado SET salario = 8000 WHERE codigo = 6;

#EXERCICIO 09 ==============================================================================================

UPDATE empregado SET setor = 3 WHERE nome = "Eduardo Monks";

#EXERCICIO 10 ==============================================================================================

UPDATE empregado SET  salario = salario + (salario*20)/100;
--ou
UPDATE empregado SET  salario = 1.2;
--caso especifico
UPDATE empregado SET  salario = 1.2 WHERE(setor = "4") OR (setor = "8") OR (setor = "5");
                                    WHERE setor IN("4","8","5");    
                                    WHERE setor IN (SELECT DISTINCT(setor) FROM empregado WHERE salario > 1500);


#EXERCICIO 11 ==============================================================================================

DELETE FROM empregado WHERE setor = "3";

#EXERCICIO 12 ==============================================================================================

DELETE  FROM empregado WHERE nome = "Gladimal Catarino"


=============================================================================================================
# EXERCICIO 2 AULA03

#EXERCICIO 01 ==============================================================================================

ALTER TABLE empregado ADD COLUMN admissao Date;

#EXERCICIO 02 ==============================================================================================

UPDATE empregado SET admissao = "2000-04-01" WHERE codigo = 1;
UPDATE empregado SET admissao = "2000-07-01" WHERE codigo = 4;
UPDATE empregado SET admissao = "2012-09-20" WHERE codigo = 7;
UPDATE empregado SET admissao = "2000-08-20" WHERE codigo = 9;
UPDATE empregado SET admissao = "2000-06-01" WHERE codigo = 10 OR codigo = 15;

#EXERCICIO 03 ==============================================================================================

SELECT * FROM empregado WHERE admissao = "2000-06-01";

#EXERCICIO 04 ==============================================================================================

SELECT * FROM empregado WHERE admissao > "2002-01-01";
SELECT NOW();

#EXERCICIO 05 ==============================================================================================

INSERT INTO empregado VALUES (16, "Eduardo Monks","3","Boss",9900, "2020-08-19");
INSERT INTO empregado VALUES (22, "Darta Inhame","3","Dev",1500, "2020-08-19");
INSERT INTO empregado VALUES (29, "Hepa Tite","3","Designer",1450, "2020-08-19");

=============================================================================================================
# EXERCICIO 3 AULA03

#EXERCICIO 01 ==============================================================================================

============================================================================================================



SELECT * FROM empregado WHERE nome LIKE "E%";
SELECT * FROM empregado WHERE nome LIKE "_A%";
SELECT * FROM empregado WHERE nome LIKE "__A%";
SELECT * FROM empregado WHERE nome LIKE "%A";

SELECT AVG(salario), MAX(salario), MIN(salario), SUM(salario), NOW();