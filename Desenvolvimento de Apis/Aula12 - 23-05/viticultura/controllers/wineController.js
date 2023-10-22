import { Wine } from "../models/Wine.js";
import { Brand } from "../models/Brand.js";
import { Op } from "sequelize";
import { Sequelize } from 'sequelize';

export const vinhoIndex = async (req, res) => {
  try {
    const vinho = await Wine.findAll({ include: Brand  });
    //lista todos os vinhos com as referidas marcas
	//apenas nome da marca
    res.status(200).json(vinho);
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
    const vinho = await Wine.create({
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

export const pesquisaVinho = async (req, res) => {
	const { pesqTipo } = req.params;

	try {
	  const pesquisa = await Wine.findAll({
		where: {
		  tipo: {
			[Op.like]: "%" + pesqTipo + "%",
		  },
		},
	  });
	  res.status(200).json(pesquisa);
	} catch (error) {
		//console.log(error);
	  res.status(400).send(error);
	}
  };

  export const tipodGrupos = async (req, res) => {
	try {
	  const tipos = await Wine.findAll({
		attributes: [
		  "tipo",
		  [Sequelize.fn("count", Sequelize.col("id")), "quant"],
		],
		group: ["tipo"],
	  });
	  res.status(200).json(tipos);
	} catch (error) {
		console.log(error);
	  res.status(400).send(error);
	}
  };