import {Cliente} from "../models/Cliente.js"
import {Produto} from "../models/Produto.js"
import { Venda } from "../models/venda.js";

export const vendaIndex = async (req, res) => {
	try {
	  const venda = await Venda.findAll(
		  { include: [Cliente, Produto]}
	  );
	  res.status(200).json(venda);
	} catch (error) {
	  res.status(400).send(error);
	}
  };