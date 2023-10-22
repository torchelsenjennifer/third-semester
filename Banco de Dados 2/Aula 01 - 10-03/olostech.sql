CREATE TABLE aluno (
id INTEGER AUTO_INCREMENT,
nome CHAR(15) NOT NULL,
idade INTEGER(4),
PRIMARY KEY(id));

CREATE TABLE disciplina (
id INTEGER AUTO_INCREMENT,
nome CHAR(15) NOT NULL,
PRIMARY KEY(id));

CREATE TABLE turma (
id_disciplina INTEGER(11),
id_aluno INTEGER(11)
);


INSERT INTO aluno (id, nome, idade) VALUES (1,'Teresa', 30);
INSERT INTO aluno (id, nome, idade) VALUES (2,'Ricardo', 18);
INSERT INTO aluno (id, nome, idade) VALUES (3,'Patricia', 20);
INSERT INTO aluno (id, nome, idade) VALUES (4,'Fabio', 37);

INSERT INTO disciplina (id, nome) VALUES (1,'Portugues');
INSERT INTO disciplina (id, nome) VALUES (2,'Matematica');
INSERT INTO disciplina (id, nome) VALUES (3,'Historia');
INSERT INTO disciplina (id, nome) VALUES (4,'Geografia');

INSERT INTO turma (id_disciplina, id_aluno) VALUES (1,1);
INSERT INTO turma (id_disciplina, id_aluno) VALUES (1,2);
INSERT INTO turma (id_disciplina, id_aluno) VALUES (1,3);
INSERT INTO turma (id_disciplina, id_aluno) VALUES (2,2);
INSERT INTO turma (id_disciplina, id_aluno) VALUES (2,4);
INSERT INTO turma (id_disciplina, id_aluno) VALUES (3,2);
INSERT INTO turma (id_disciplina, id_aluno) VALUES (3,3);
INSERT INTO turma (id_disciplina, id_aluno) VALUES (3,4);

SELECT aluno.id, aluno.nome, aluno.idade
from turma, aluno
WHERE aluno.id = turma.id_aluno 
ORDER BY aluno.nome

SELECT aluno.id, aluno.nome, aluno.idade
from turma, aluno
WHERE aluno.id =turma.id_aluno AND turma.id_disciplina = 2
ORDER BY aluno.nome

