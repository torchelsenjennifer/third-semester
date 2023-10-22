import { sequelize } from "../databases/conecta.js";
import { Cardapio } from "../models/Cardapio.js";
import { Op } from "sequelize";

export const cardapioIndex = async (req, res) => {
  try {
    const cardapios = await Cardapio.findAll();
    res.status(200).json(cardapios);
  } catch (error) {
    res.status(400).send(error);
  }
};

export const cardapioCreate = async (req, res) => {
  const { prato, categoria, preco, calorias } = req.body;

  if (!prato || !categoria || !preco || !calorias) {
    res.status(400).json({
      id: 0,
      msg: "Erro... Informe prato, categoria, preco e calorias do cardapio.",
    });
    return;
  }

  try {
    const cardapio = await Cardapio.create({
      prato,
      categoria,
      preco,
      calorias,
    });
    res.status(201).json(cardapio);
  } catch (error) {
    res.status(400).send(error);
  }
};

export const cardapioUpdate = async (req, res) => {
  const { id } = req.params;
  const { prato, categoria, preco, calorias } = req.body;

  if (!prato || !categoria || !preco || !calorias) {
    res.status(400).json({
      id: 0,
      msg: "Erro... Informe prato, categoria, preço e calorias do cardapio.",
    });
    return;
  }

  try {
    const cardapio = await Cardapio.update(
      {
        prato,
        categoria,
        preco,
        calorias,
      },
      {
        where: { id },
      }
    );
    res.status(200).json(cardapio);
  } catch (error) {
    res.status(400).send(error);
  }
};

export const cardapioDestroy = async (req, res) => {
  const { id } = req.params;
  try {
    const cardapio = await Cardapio.destroy({
      where: { id },
    });
    res.status(200).json(cardapio);
  } catch (error) {
    res.status(400).send(error);
  }
};

export const cardapioPrato = async (req, res) => {
  const { prato } = req.params;

  try {
    const cardapios = await Cardapio.findAll({
      where: {
        prato: {
          [Op.like]: "%" + prato + "%",
        },
      },
    });
    res.status(200).json(cardapios);
  } catch (error) {
    res.status(400).send(error);
  }
};

//Que o preço seja igual ou inferior ao informado como parâmetro
//=========================================================================
export const cardapioPreco = async (req, res) => {
  const { preco } = req.params;

  try {
    console.log(preco);
    const cardapios = await Cardapio.findAll({
      where: {
        preco: {
          [Op.lte]: preco,
        },
      },
    });
    res.status(200).json(cardapios);
  } catch (error) {
    res.status(400).send(error);
  }
};

//==================================================================================

export const cresenteCaloria = async (req, res) => {
  try {
    const cardapios = await Cardapio.findAll({
      order: [["calorias", "ASC"]],
    });

    res.status(200).json(cardapios);
  } catch (error) {
    res.status(400).send(error);
  }
};

export const mediaEstatistica = async (req, res) => {
  try {
    const pratos = await Cardapio.count();
    const precosSoma = await Cardapio.sum("preco");
    res.status(200).json({
      mediaPratos: Math.round(precosSoma / pratos),
    });
  } catch (error) {
    res.status(400).send(error);
  }
};

//Preço médio dos pratos da categoria passada como parâmetro
  export const mediaCategoria = async (req, res) => {
	const { pesquisa } = req.params;

	try {

	  const somaCategoria = await Cardapio.sum("preco", {
		where: {
			categoria: {
			  [Op.like]: "%" + pesquisa + "%",
			},
		  },
	  });

	  const quantidadePratos = await Cardapio.count( {
		where: {
			categoria: {
			  [Op.like]: "%" + pesquisa + "%",
			},
		  },
	  });
	  res.status(200).json({
		mediaCategoria: (somaCategoria / quantidadePratos).toFixed(2),
	  });
	} catch (error) {
	  res.status(400).send(error);
	}
  };

export const cardapiodGrupos = async (req, res) => {
  try {
    const cardapios = await Cardapio.findAll({
      attributes: [
        "categoria",
        [sequelize.fn("count", sequelize.col("id")), "quant"],
      ],
      group: ["categoria"],
    });
    res.status(200).json(cardapios);
  } catch (error) {
    res.status(400).send(error);
  }
};
