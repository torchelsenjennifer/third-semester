import { Brand } from "../models/Brand.js";
import { Wine } from "../models/Wine.js";
import { Op } from "sequelize";
import { Sequelize } from 'sequelize';

export const marcaIndex = async (req, res) => {
	try {
	  const marca = await Brand.findAll({ include: Wine });
		// retorna todos os vinhos da referida marca
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
	  const marca = await Brand.create({
		nome,
		cidade,
	  });
	  res.status(201).json(marca);
	} catch (error) {
	  res.status(400).send(error);
	}
  };

  export const pesquisaMarca = async (req, res) => {
	const { pesqMarca } = req.params;

	try {
	  const pesquisa = await Brand.findAll({
		where: {
		  nome: {
			[Op.like]: "%" + pesqMarca + "%",
		  },
		},
	  });
	  res.status(200).json(pesquisa);
	} catch (error) {
		//console.log(error);
	  res.status(400).send(error);
	}
  };

  export const nomedGrupos = async (req, res) => {
	try {
	  const nomes = await Brand.findAll({
		attributes: [
		  "nome",
		  [Sequelize.fn("count", Sequelize.col("id")), "quant"],
		],
		group: ["nome"],
	  });
	  res.status(200).json(nomes);
	} catch (error) {
		console.log(error);
	  res.status(400).send(error);
	}
  };
