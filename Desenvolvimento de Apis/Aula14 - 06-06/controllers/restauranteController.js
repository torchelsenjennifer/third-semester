import { sequelize } from "../databases/conecta.js";
import { Usuario } from "../models/Usuario.js";
import { Restaurante } from "../models/Restaurante.js";

export const restauranteIndex = async (req, res) => {
  try {
    const restaurantes = await Restaurante.findAll({ include: Usuario });
    res.status(200).json(restaurantes);
  } catch (error) {
    res.status(400).send(error);
  }
};

export const restauranteCreate = async (req, res) => {
  const { nome, usuario_id } = req.body;

  if (!nome || !usuario_id) {
    res.status(400).json({
      id: 0,
      msg: "Erro...Informe os dados.",
    });
    return;
  }
  try {
    const restaurante = await Restaurante.create({
      nome,
      usuario_id,
    });
    res.status(201).json(restaurante);
  } catch (error) {
    res.status(400).send(error);
  }
};

export const restauranteDestroy = async (req,res) =>{
	const {id} = req.params
	try{
		await Restaurante.destroy({ where: {id}});

		await Log.create({
			descricao: "Exclusao do Restaurante " + id,
			usuario_id: 1
		})
		res.status(200).json({ msg: "oK! Removido com Sucesso"})
	}catch(error){
		res.status(400).send(error)
	}
  }
