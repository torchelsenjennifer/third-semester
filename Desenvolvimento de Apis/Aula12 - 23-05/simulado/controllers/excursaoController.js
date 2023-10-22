import { Destino } from "../models/Destino.js";
import { Excursao } from "../models/Excursao.js";

export const excursaoIndex = async (req, res) => {
  try {
    const excursao = await Excursao.findAll(
      { include: [Destino] }
      //inclusao para aparecer na listagem carro e cliente
    );
    res.status(200).json(excursao);
  } catch (error) {
    res.status(400).send(error);
  }
};

export const excursaoCreate = async (req, res) => {
  const { dataPartida, preco, quant_lugares, destino_id } = req.body;

  if (!dataPartida || !preco || !quant_lugares || !destino_id) {
    res.status(400).json({
      id: 0,
      msg: "Erro...Informe os dados.",
    });
    return;
  }
  try {
    const excursao = await Excursao.create({
      dataPartida,
      preco,
      quant_lugares,
      destino_id,
    });
    res.status(201).json(excursao);
  } catch (error) {
    res.status(400).send(error);
  }
};
