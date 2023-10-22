import { Carro } from "../models/Carro.js";
import { Cliente } from "../models/Cliente.js";
import { Proposta } from "../models/Proposta.js";

export const propostaIndex = async (req, res) => {
  try {
    const proposta = await Proposta.findAll(
		{ include: [Carro, Cliente]}
	);
    res.status(200).json(proposta);
  } catch (error) {
    res.status(400).send(error);
  }
};

export const propostaCreate = async (req, res) => {
  const { cliente_id, carro_id, descricao } = req.body;

  if (!cliente_id || !carro_id || !descricao) {
    res.status(400).json({
      id: 0,
      msg: "Erro...Informe os dados.",
    });
    return;
  }
  try {
    const proposta = await Proposta.create({
      cliente_id,
      carro_id,
      descricao,
    });
    res.status(201).json(proposta);
  } catch (error) {
    res.status(400).send(error);
  }
};
