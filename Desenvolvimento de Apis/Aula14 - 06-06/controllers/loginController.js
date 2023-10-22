import bcrypt from "bcrypt";
import jwt from "jsonwebtoken";

import * as dotenv from "dotenv";
dotenv.config();

import { Usuario } from "../models/Usuario.js";

export const loginUsuario = async (req, res) => {
  const { email, senha } = req.body;

  if (!email || !senha) {
    res.status(400).json({ erro: "Informe e-mail e senha de acesso" });
    return;
  }

  try {
    const usuario = await Usuario.findOne({ where: { email } });

    if (usuario == null) {
      res.status(400).json({ erro: "Erro... E-mail invalido" });
      return;
    }

    if (bcrypt.compareSync(senha, usuario.senha)) {
      const token = jwt.sign(
        {
          user_logado_id: usuario.id,
          user_logado_nome: usuario.nome,
        },
        process.env.JWT_KEY,
        { expiresIn: "1h" }
      );

      res.status(200).json({ msg: "Ok. Logado", token });
    } else {
      res.status(400).json({ erro: "Erro... Senha Invalida" });
    }
  } catch {
    res.status(400).json(erro);
  }
};
