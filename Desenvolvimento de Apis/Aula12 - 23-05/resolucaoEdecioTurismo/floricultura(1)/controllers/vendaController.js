import { Venda } from '../models/Venda.js'
import { Cliente } from '../models/Cliente.js'

export const vendaIndex = async (req, res) => {
  try {
    const vendas = await Venda.findAll({
      include: Cliente
    });
    res.status(200).json(vendas)
  } catch (error) {
    res.status(400).send(error)
  }
}

export const vendaCreate = async (req, res) => {
  const { cliente_id, data } = req.body

  // se não informou estes atributos
  if (!cliente_id || !data) {
    res.status(400).json({ id: 0, msg: "Erro... Informe os dados" })
    return
  }

  try {
    const venda = await Venda.create({
      cliente_id, data
    });
    res.status(201).json(venda)
  } catch (error) {
    res.status(400).send(error)
  }
}
