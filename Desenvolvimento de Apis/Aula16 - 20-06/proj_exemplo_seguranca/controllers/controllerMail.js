"use strict";
import nodemailer from "nodemailer";
import { Usuario } from "../models/Usuario";
import md5 from "md5";

// async..await is not allowed in global scope, must use a wrapper
async function main(nome, email, hash) {

  // create reusable transporter object using the default SMTP transport
  let transporter = nodemailer.createTransport({
    host: "sandbox.smtp.mailtrap.io",
    port: 2525,
    secure: false, // true for 465, false for other ports
    auth: {
      user: "bd0c95a92862ec", // generated ethereal user
      pass: "01a7473cb832c7", // generated ethereal password
    },
  });

	const link = "http://localhost:3000/trocasenha/"+hash

	let mensa = "<h5>Sistema de Avaliação de Restaurantes</h5>"
	mensa += `<h6>Estimado: ${nome} </h6>`
	mensa += "<h6>Você solicitou a troca de senha. "
	mensa += "Clique no link abaixo para alterar:</h6>"
	mensa += `<a href="${link}">Aterar sua senha</a>`



  // send mail with defined transport object
  let info = await transporter.sendMail({
    from: '"Sistema Avaliação Restaurante" <loveDaJennifer.com>', // sender address
    to: email, // list of receivers
    subject: "Solicitação de Alteração de Senha", // Subject line
    text: `Copie e cole o endereço: ${link}`, // plain text body
    html: mensa, // html body
  });

  console.log("Message sent: %s", info.messageId);
  // Message sent: <b658f8ca-6296-ccf4-8306-87d57a0b4321@example.com>

  // Preview only available when sending through an Ethereal account
  console.log("Preview URL: %s", nodemailer.getTestMessageUrl(info));
  // Preview URL: https://ethereal.email/message/WaQKMgKddxQDoou...
}

export const enviaEmail = async (req, res) => {
	const { email, senha, novaSenha } = req.body

	// se nÃ£o informou estes atributos
	if (!email || !senha || !novaSenha) {
	  res.status(400).json({ id: 0, msg: "Erro... Informe os dados" })
	  return
	}

	try {
	  const usuario = await Usuario.findOne({ where: { email } })

	  if (usuario == null) {
		res.status(400).json({ erro: "Erro... E-mail invÃ¡lido" })
		return
	  }
	  const hash = md5(usuario.nome + email + Date.now())
	  main(usuario.nome, email, hash).catch(console.error);

	  res.status(200).json({ msg: "ok. Email para alteração enviado com sucesso!" })
  }catch (error) {
    res.status(400).json(error)
  }
}
