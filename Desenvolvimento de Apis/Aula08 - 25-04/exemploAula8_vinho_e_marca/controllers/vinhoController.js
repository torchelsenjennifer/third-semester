import { Vinho } from "../models/Vinho.js";
import {Marca} from "../models/Marca.js"

export const vinhoIndex = async (req, res) => {
  try {
    const vinhos = await Vinho.findAll({ include: Marca });
    res.status(200).json(vinhos);
  } catch (error) {
    res.status(400).send(error);
  }
};

export const vinhoCreate = async (req, res) => {
  const { tipo, preco, teor, marca_id } = req.body;

  if (!tipo || !preco || !teor || !marca_id) {
    res.status(400).json({
      id: 0,
      msg: "Erro...Informe os dados.",
    });
    return;
  }

  try {
    const vinho = await Vinho.create({
      tipo,
      preco,
      teor,
      marca_id,
    });
    res.status(201).json(vinho);
  } catch (error) {
    res.status(400).send(error);
  }
};
