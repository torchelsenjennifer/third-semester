import { sequelize } from '../databases/conecta.js'

import { VendaProduto } from '../models/VendaProduto.js'
import { Venda } from '../models/Venda.js'
import { Produto } from '../models/Produto.js'
import { request } from 'express'

export const vendaProdutoIndex = async (req, res) => {
  const { id } = req.params

  try {
    const vendaProdutos = await VendaProduto.findAll({
      include: Produto, where: { venda_id: id }
    });
    res.status(200).json(vendaProdutos)
  } catch (error) {
    res.status(400).send(error)
  }
}

export const vendaProdutoCreate = async (req, res) => {
  const { venda_id, produto_id, quant, preco } = req.body

  // se não informou estes atributos
  if (!venda_id || !produto_id || !quant || !preco) {
    res.status(400).json({ id: 0, msg: "Erro... Informe os dados" })
    return
  }

  const t = await sequelize.transaction();

  try {

    const vendaProduto = await VendaProduto.create({
      venda_id, produto_id, quant, preco
    }, { transaction: t });

    await Produto.decrement('quant',
      { by: quant, where: { id: produto_id }, transaction: t }
    );

    // await Venda.update(
    //   { total: sequelize.literal(`total + ${quant*preco}`) },
    //   { where: { id: venda_id }, transaction: t }
    // );

    await Venda.increment('total',
      { by: quant*preco, where: { id: venda_id }, transaction: t }
    );

    await t.commit();
    res.status(201).json(vendaProduto)

  } catch (error) {

    await t.rollback();
    res.status(400).json({"id": 0, "Erro": "Erro... verifique a quantidade em estoque"})

  }
}