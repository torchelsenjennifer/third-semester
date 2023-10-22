DROP SCHEMA IF EXISTS aula04;
CREATE SCHEMA IF NOT EXISTS aula04;
USE aula04;

DROP TABLE IF EXISTS produtos;

CREATE TABLE IF NOT EXISTS produtos(
    referencia VARCHAR(3) NOT NULL,
    descricao VARCHAR(50)  NULL DEFAULT NULL,
    estoque INT(11) NOT NULL DEFAULT 0,
    PRIMARY KEY (referencia)
);

INSERT INTO produtos (referencia, descricao, estoque) VALUES ('001', 'Feijão', 10);
INSERT INTO produtos (referencia, descricao, estoque) VALUES ('002', 'Arroz', 5);
INSERT INTO produtos (referencia, descricao, estoque) VALUES ('003', 'Farinha', 15);

DROP TABLE IF EXISTS itemVenda;

CREATE TABLE IF NOT EXISTS itemVenda(
    venda INT(11) NULL DEFAULT NULL,
    produtos VARCHAR(3) NULL DEFAULT NULL,
    quantidade INT(11) NULL DEFAULT NULL,
    CONSTRAINT fk_itensVenda_produtos
        FOREIGN KEY (produtos) REFERENCES produtos (referencia) ON DELETE NO ACTION ON UPDATE NO ACTION
);

INSERT INTO itemVenda VALUES(1, '003', 2);

DELIMITER $$

CREATE TRIGGER trg_itemVenda_AI AFTER INSERT
ON itemVenda
FOR EACH ROW
BEGIN
    UPDATE produtos SET estoque = estoque - NEW.quantidade WHERE referencia = NEW.produtos;
END $$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER trg_itemVenda_AD AFTER DELETE
ON itemVenda
FOR EACH ROW
BEGIN
    UPDATE produtos SET estoque = estoque + OLD.quantidade WHERE referencia = OLD.produtos;
END$$

DELIMITER;

-- apaga as vendas
DELETE FROM itemVenda WHERE venda = 1 AND produtos = '001';
