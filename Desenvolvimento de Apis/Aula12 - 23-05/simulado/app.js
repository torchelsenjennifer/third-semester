import express from "express";
import cors from "cors";
import routes from "./routes.js";

import { sequelize } from "./databases/conecta.js";
import { Destino } from "./models/Destino.js";
import { Cliente } from "./models/Cliente.js";
import { Excursao } from "./models/Excursao.js";
import { Reserva } from "./models/Reserva.js";

const app = express();
const port = 3000;

app.use(express.json());
app.use(cors());
app.use(routes);

async function conecta_db() {
  try {
    await sequelize.authenticate();
    console.log("Conexão com Banco de dados Realizada com sucesso");
    //await sequelize.sync({alter:true}); //-> Verifica se ha alterações e atualiza as tabelas se houver
    //await sequelize.sync({force:true}); // -> recria as tabelas, mesmo se já existirem
	await Destino.sync();
	await Cliente.sync(); //{alter: true}
	await Excursao.sync();
	await Reserva.sync();

  } catch (erro) {
    console.log(erro);
    console.error("Erro na conexão com o banco");
  }
}

conecta_db();

app.get("/", (req, res) => {
  res.send("Atividade : API Agencia de Turismo");
});

app.listen(port, () => {
  console.log(`Rodando na porta: ${port}`);
});
