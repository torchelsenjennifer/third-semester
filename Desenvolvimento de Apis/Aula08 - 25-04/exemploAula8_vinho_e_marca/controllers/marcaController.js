import { Marca } from "../models/Marca.js";
import { Vinho } from "../models/Vinho.js";

export const marcaIndex = async (req, res) => {
  try {
    const marca = await Marca.findAll({ include: Vinho });
    res.status(200).json(marca);
  } catch (error) {
    res.status(400).send(error);
  }
};

export const marcaCreate = async (req, res) => {
  const { nome, cidade } = req.body;

  if (!nome || !cidade) {
    res.status(400).json({
      id: 0,
      msg: "Erro...Informe os dados.",
    });
    return;
  }

  try {
    const marca = await Marca.create({
      nome,
      cidade,
    });
    res.status(201).json(marca);
  } catch (error) {
    res.status(400).send(error);
  }
};
