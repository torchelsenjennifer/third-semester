import { Produto } from "../models/Produto.js";

export const produtoIndex = async (req, res) => {
  try {
    const produtos = await Produto.findAll();
    res.status(200).json(produtos);
  } catch (erro) {
    res.status(400).send(erro);
  }
};

export const produtoCreate = async (req, res) => {
    const {descricao, marca, quant, preco} = req.body
    try {
        descricao,
        marca,
        quant,
        preco
    } catch (erro) {
      res.status(400).send(erro);
    }
  };
  