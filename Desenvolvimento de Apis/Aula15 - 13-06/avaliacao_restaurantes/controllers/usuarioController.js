import { Usuario } from '../models/Usuario.js'

export const usuarioIndex = async (req, res) => {
  try {
    const usuarios = await Usuario.findAll();
    res.status(200).json(usuarios)
  } catch (error) {
    res.status(400).send(error)
  }
}

export const usuarioCreate = async (req, res) => {
  const { nome, email, senha } = req.body

  // se não informou estes atributos
  if (!nome || !email || !senha) {
    res.status(400).json({ id: 0, msg: "Erro... Informe os dados" })
    return
  }

  try {
    const usuario = await Usuario.create({
      nome, email, senha
    });
    res.status(201).json(usuario)
  } catch (error) {
    res.status(400).send(error)
  }
}
