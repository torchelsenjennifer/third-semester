CREATE table teste(
    codigo INT,
    nome CHAR(15),
    email VARCHAR(30),
    PRIMARY KEY(codigo)
);

ALTER TABLE teste
    ADD endereco CHAR(50)
    AFTER nome;

ALTER TABLE teste ADD nascimento Date;

ALTER table teste MODIFY email CHAR(40);
-- MODIFCA O VALOR
ALTER table teste CHANGE email e_email CHAR(30);
-- ALTERA O NOME
ALTER TABLE teste DROP codigo;

ALTER TABLE teste ADD PRIMARY KEY (nome);

ALTER TABLE teste DROP PRIMARY KEY;

ALTER TABLE teste RENAME TO teste2;

DROP TABLE teste2;