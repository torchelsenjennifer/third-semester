import { sequelize } from '../databases/conecta.js';
import { Op } from "sequelize"
import { Carro } from '../models/Carro.js'

export const carroIndex = async (req, res) => {
  try {
    const carros = await Carro.findAll();
    res.status(200).json(carros)
  } catch (error) {
    res.status(400).send(error)
  }
}

export const carroCreate = async (req, res) => {
  const { modelo, marca, ano, preco, placa } = req.body

  // se não informou estes atributos
  if (!modelo || !marca || !ano || !preco || !placa) {
    res.status(400).json({ id: 0, msg: "Erro... Informe modelo, marca, ano, placa e preco do Carro." })
    return
  }

  try {
    const carro = await Carro.create({
      modelo, marca, ano, preco, placa
    });
    res.status(201).json(carro)
  } catch (error) {
    res.status(400).send(error)
  }
}

export const carroStatus = async (req, res) => {
  const valor = req.params.valor.toUpperCase()

  const anoAtual = new Date().getFullYear()
  let inicial
  let final

  if (valor == "NOVO") {
    inicial = anoAtual
    final = anoAtual
  } else if (valor == "SEMI-NOVO") {
    inicial = anoAtual - 2
    final = anoAtual - 1
  } else {
    inicial = 1000
    final = anoAtual - 3
  }

  try {
    const carros = await Carro.findAll({
      where: {
        ano: {
          [Op.between]: [inicial, final]
        }
      }
    });
    res.status(200).json(carros)
  } catch (error) {
    res.status(400).send(error)
  }
}

export const carroGrupos = async (req, res) => {
  try {
    const carros = await Carro.findAll({
      attributes: [
        'marca',
        [sequelize.fn('count', sequelize.col('id')), 'quant'],
      ],
      group: ['marca']
    });
    res.status(200).json(carros)
  } catch (error) {
    res.status(400).send(error)
  }
}
