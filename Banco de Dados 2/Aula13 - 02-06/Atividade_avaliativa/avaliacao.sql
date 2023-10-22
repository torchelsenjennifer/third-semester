--========================================================================================================================
--1. Crie um banco de dados chamado aula13.
DROP DATABASE IF EXISTS aula13;
CREATE DATABASE aula13;
USE aula13;

--==========================================================================================================================
--2. No banco aula13 crie as tabelas conforme o diagrama
CREATE TABLE usuario(
  id	INT NOT NULL AUTO_INCREMENT,
  nome	VARCHAR(45) NULL,
  email VARCHAR(255) NULL,
  fone 	INT(20) NULL,
  PRIMARY KEY (id)
);

CREATE TABLE forum(
  id	INT NOT NULL AUTO_INCREMENT,
  titulo VARCHAR(45) NULL,
  data_criacao DATE NOT NULL,
  PRIMARY KEY (id),
);

CREATE TABLE postagem(
  id         INT NOT NULL AUTO_INCREMENT,
  mensagem     text NULL,
  data_postagem DATE NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_usuario   FOREIGN KEY (usuario_id)   REFERENCES usuario (id)   ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_forum FOREIGN KEY (forum_id) REFERENCES forum (id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- ============================================================================================================================================
-- 3. Crie um usu�rio chamado moderador, com a senha 123teste. Este usu�rio poder� acessar as 3 tabelas com permiss�o de INSERT, UPDATE e DELETE
CREATE USER 'moderador'@'localhost' IDENTIFIED BY 'teste123'
GRANT INSERT, UPDATE, DELETE ON aula13.usuario TO moderador@localhost;
GRANT INSERT, UPDATE, DELETE ON aula13.forum TO moderador@localhost;
GRANT INSERT, UPDATE, DELETE ON aula13.postagem TO moderador@localhost;
FLUSH PRIVILEGES;

--===========================================================================================================================================
--4. Crie um usu�rio chamado pikachu, com a senha teste123. Este usu�rio poder� somente fazer SELECT no campo mensagem da tabela postagem.
CREATE USER 'pikachu'@'localhost' IDENTIFIED BY 'teste123';
GRANT SELECT (mensagem) ON aula13.postagem TO 'pikachu'@'localhost';
FLUSH PRIVILEGES;

--=============================================================================================================================================
--5. Crie um usu�rio chamado maverick, com a senha topgun. Este usu�rio poder� fazer INSERT, UPDATE e DELETE nas tabelas f�rum e postagem. Ele
--tamb�m poder� fazer SELECT na tabela usu�rio.
CREATE USER 'maverick'@'localhost' IDENTIFIED BY 'topgun';
GRANT INSERT, UPDATE, DELETE ON aula13.forum TO maverick@localhost;
GRANT INSERT, UPDATE, DELETE ON aula13.postagem TO maverick@localhost;
GRANT SELECT ON aula13.usuario TO maverick@localhost;

--==============================================================================================================================================
--6. Com o usu�rio moderador, fa�a inser��o de registros nas tabelas forum e usuario (pelo menos 8 registros na tabela usuario e 5 registros na tabela
--forum).

--Usuario moderador
INSERT TO usuario(nome, email, fone) VALUES ('jennifer torchelsen', 'jennifer@gmail.com', '53981052090');
INSERT TO usuario(nome, email, fone) VALUES ('jonas torchelsen', 'jonas@gmail.com', '5398214579');
INSERT TO usuario(nome, email, fone) VALUES ('jonathan torchelsen', 'jonathan@gmail.com', '53981130593');
INSERT TO usuario(nome, email, fone) VALUES ('jessica torchelsen', 'jessica@gmail.com', '53981020194');
INSERT TO usuario(nome, email, fone) VALUES ('joao torchelsen', 'joao@gmail.com', '53999822088');
INSERT TO usuario(nome, email, fone) VALUES ('jose torchelsen', 'jose@gmail.com', '53984042496');
INSERT TO usuario(nome, email, fone) VALUES ('paula torchelsen', 'paula@gmail.com', '53981254198');
INSERT TO usuario(nome, email, fone) VALUES ('julia torchelsen', 'julia@gmail.com', '53984252123');

INSERT TO forum(titulo, data_criacao) VALUES ('atividade banco de dados', '2023-06-09');
INSERT TO forum(titulo, data_criacao) VALUES ('d�vidas', '2023-06-09');
INSERT TO forum(titulo, data_criacao) VALUES ('discutindo banco de dados', '2023-06-09');
INSERT TO forum(titulo, data_criacao) VALUES ('reavaliacao de banco de dados', '2023-06-09');
INSERT TO forum(titulo, data_criacao) VALUES ('avaliando prova de banco de dados', '2023-06-09');

--=============================================================================================================================================
--7. Com o usu�rio root consulte o conte�do das tabelas f�rum e usu�rio; (tente fazer as mesmas consultas com os usu�rios moderador, pikachu e
--maverick)

--============================================================================================================================================
--8. Com o usu�rio maverick, insira 10 registros na tabela postagem (as postagens dever�o ser de 6 usu�rios diferentes).
--usuario maverick
INSERT TO postagem(mensagem, data_postagem, forum_id, usuario_id) VALUES ('muito dificil', '2023-06-09', 1, 1 );
INSERT TO postagem(mensagem, data_postagem, forum_id, usuario_id) VALUES ('muito facil', '2023-06-09', , 2);
INSERT TO postagem(mensagem, data_postagem, forum_id, usuario_id) VALUES ('mais ou menos', '2023-06-09', 3, 3);
INSERT TO postagem(mensagem, data_postagem, forum_id, usuario_id) VALUES ('muito difici�', '2023-06-09', 4, 4);
INSERT TO postagem(mensagem, data_postagem, forum_id, usuario_id) VALUES ('muito facil', '2023-06-09', 5, 5);
INSERT TO postagem(mensagem, data_postagem, forum_id, usuario_id) VALUES ('mais ou menos', '2023-06-09', 1, 6);
INSERT TO postagem(mensagem, data_postagem, forum_id, usuario_id) VALUES ('muito dificil', '2023-06-09', 2, 7);
INSERT TO postagem(mensagem, data_postagem, forum_id, usuario_id) VALUES ('mais ou menos', '2023-06-09', 3, 8);
INSERT TO postagem(mensagem, data_postagem, forum_id, usuario_id) VALUES ('muito dificil', '2023-06-09', 4, 1);
INSERT TO postagem(mensagem, data_postagem, forum_id, usuario_id) VALUES ('mais ou menos', '2023-06-09', 5, 2);


--9. Com o usu�rio root consulte o conte�do da tabela postagem; (tente fazer a mesma consulta com os usu�rios moderador, pikachu e maverick)

--10. Com o usu�rio moderador, fa�a uma consulta que retorne: t�tulo do f�rum, nome do usu�rio e data da postagem

--11. Com o usu�rio pikachu, tente fazer a mesma consulta da quest�o anterior (exiba o print da consulta e o resultado obtido).

--12. Acesse o banco com o usu�rio root (ou algum usu�rio com permiss�es de superadmin)

--13. Verifique se o autocommit do banco est� ativo ou n�o (exiba o comando)
SHOW VARIABLES LIKE 'autocommit';

--14. Desabilite o autocommit
SET autocommit = 0;

--15. Fa�a uma consulta (SELECT) de todos os registros da tabela postagem
SELECT *
FROM postagem;

--16. Inicie uma transa��o
START TRANSACTION;

--17. Insira 1 novo registro a tabela postagem
INSERT TO postagem(mensagem, data_postagem, forum_id, usuario_id) VALUES ('eu tirei A', '2023-06-09', 1, 1);

--18. Fa�a, novamente, uma consulta (SELECT) de todos os registros da tabela postagem
SELECT *
FROM postagem;

--19. Execute um rollback da transa��o.
ROLLBACK;

--20. Fa�a, novamente, uma consulta (SELECT) de todos os registros da tabela postagem
SELECT *
FROM postagem;

--21. Inicie uma transa��o
START TRANSACTION;

--22. Fa�a, novamente, uma consulta (SELECT) de todos os registros da tabela postagem
SELECT *
FROM postagem;

--23. Insira 1 novo registro a tabela postagem
INSERT TO postagem(mensagem, data_postagem, forum_id, usuario_id) VALUES ('eu tirei B', '2023-06-09', 2, 2);

--24. Fa�a, novamente, uma consulta (SELECT) de todos os registros da tabela postagem
SELECT *
FROM postagem;

--25. Execute o commit da transa��o.
COMMIT;
--26. Fa�a, novamente, uma consulta (SELECT) de todos os registros da tabela postagem
SELECT *
FROM postagem;

--27. Tente realizar um rollback e fa�a, novamente, uma consulta (SELECT) de todos os registros da tabela postagem
ROLLBACK;
SELECT *
FROM postagem;

--28. Habilite o autocommit
SET autocommit = 1;

--29. Exclua o usu�rio maverick
DROP USER 'maverick'@'localhost';

--30. Exclua o usu�rio pikachu
DROP USER 'pikachu'@'localhost';

--31. Exclua o usu�rio moderador
DROP USER 'usuario'@'localhost';

--32. Fa�a uma consulta que exiba o t�tulo das postagens dos usu�rios que o nome (nome do usu�rio) tenha a letra ?a?.
--duvida