import { sequelize } from '../databases/conecta.js'
import { Cliente } from '../models/Cliente.js';
import { Excursao } from "../models/Excursao.js";
import { Reserva } from "../models/Reserva.js";

export const reservaIndex = async (req, res) => {
  try {
    const reserva = await Reserva.findAll(
       { include: [Cliente] }
      //inclusao para aparecer na listagem carro e cliente
    );
    res.status(200).json(reserva);
  } catch (error) {
    res.status(400).send(error);
  }
};

export const reservaCreate = async (req, res) => {
  const { quantComprados, precoTotal, cliente_id, excursao_id } = req.body;

  if (!quantComprados || !precoTotal || !cliente_id || !excursao_id) {
    res.status(400).json({
      id: 0,
      msg: "Erro...Informe os dados.",
    });
    return;
  }
  //começa a transação
  const t = await sequelize.transaction();

  try {
    const reserva = await Reserva.create(
      {
        quantComprados,
        precoTotal,
        cliente_id,
        excursao_id,
      },
      { transaction: t }
    );

    await Excursao.increment("lugares_reservados", {
      by: quantComprados,
      where: { id: excursao_id },
      transaction: t,
    });

    await t.commit();
    res.status(201).json(reserva);
  } catch (error) {
	await t.rollback();
    res.status(400).json({"id": 0, "Erro": error})
	console.log(error)
  }
};
