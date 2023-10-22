/* 1 Crie um usuário chamado rimidalg, com a senha cheesebebum.
Este usuário poderá acessar as 3 tabelas SOMENTE com permissão de SELECT, INSERT, UPDADE e DELETE.*/

CREATE USER 'rimidalg'@'localhost' IDENTIFIED BY 'cheesebebum'
GRANT SELECT, INSERT, UPDATE, DELETE ON aula18.UF TO rimidalg@localhost;
GRANT SELECT, INSERT, UPDATE, DELETE ON aula18.CIDADE TO rimidalg@localhost;
GRANT SELECT, INSERT, UPDATE, DELETE ON aula18.ATLETA TO rimidalg@localhost;
FLUSH PRIVILEGES;


/* 2 Crie um usuário chamado arnlod, com a senha cheesesalada.
Este usuário poderá somente fazer SELECT no campo apelido da tabela atleta. */
CREATE USER 'arnlod'@'localhost' IDENTIFIED BY 'cheesesalada'
GRANT SELECT (apelido) ON aula13.ATLETA TO 'arnlod'@'localhost';
FLUSH PRIVILEGES;

/* 3 Crie um usuário chamado oicede, com a senha ovoebacon.
Este usuário poderá fazer SELECT e INSERT na tabela atleta.
Ele também poderá fazer SELECT na tabela cidade.*/
CREATE USER 'oicede'@'localhost' IDENTIFIED BY 'ovoebacon'
GRANT SELECT, INSERT ON aula13.ATLETA TO 'oicede'@'localhost';
GRANT SELECT ON aula18.CIDADE TO 'oicede'@'localhost';
FLUSH PRIVILEGES;

/*4 Tire, do usuário oicede, a permissão de INSERT na tabela atleta*/
REMOVE INSERT ON aula18.atleta FROM '[oicede]'@'localhost'


/*=====================questao dois===========================================*/
/*1. Qual o comando para visualizar os bancos de dados existentes?*/
SHOW DATABASE

/*2. Qual o comando para criar um banco de dados chamado "SENAC"?*/
USE SENAC

/*3. Qual o comando para verificar as coleções existentes?*/
SHOW COLLECTIONS

/*4. Qual o comando para criar uma coleção chamada "Contatos" já contendo um documento com as seguintes informações: nome: "Angelo", telefone: "190"?*/
db.contatos.insert({nome: "Angelo", telefone: "190" })

/*5. Qual o comando (ou quais os comandos) para inserir, na coleção "Contatos", os dados a seguir

Edecio - 99
Gladimir - 123*/

db.contatos.insert({nome: "Edecio", telefone: "99" })
db.contatos.insert({nome: "Gladimir", telefone: "123" })

/*6. Qual o comando para pesquisar e retornar todos os contatos?*/

db.contatos.find()

/*7. Qual o comando retornar a quantidade total de contatos?*/
