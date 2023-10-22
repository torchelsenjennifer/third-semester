import { sequelize } from "../databases/conecta.js";
import { Restaurante } from "../models/Restaurante.js";
import { Usuario } from "../models/Usuario.js";

export const usuarioIndex = async (req, res) => {
  try {
    const usuarios = await Usuario.findAll();
    res.status(200).json(usuarios);
  } catch (error) {
    res.status(400).send(error);
  }
};

export const usuarioCreate = async (req, res) => {
	const { nome, email, senha } = req.body;

	if (!nome || !email || !senha) {
	  res.status(400).json({
		id: 0,
		msg: "Erro...Informe os dados.",
	  });
	  return;
	}
	try {
	  const usuarios = await Usuario.create({
		nome, email, senha
	  });
	  res.status(201).json(usuarios);
	} catch (error) {
	  res.status(400).send(error);
	}
  };

  export const restauranteDestroy = async (req,res) =>{
	const {id} = req.params
	try{
		await Restaurante.destroy({ where: {id}});
		res.status(200).json({ msg: "oK! Removido com Sucesso"})
	}catch(error){
		res.status(400).send(error)
	}
  }