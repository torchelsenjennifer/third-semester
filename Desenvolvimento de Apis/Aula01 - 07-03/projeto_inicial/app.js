import express from "express";
import { sequelize } from "./databases/conecta.js";

const app = express();
const port = 3000;

import routes from "./routes.js";

app.use(express.json());
app.use(routes);

async function conecta_db() {
  try {
    await sequelize.authenticate();
    console.log("Conexao com o banco de dados relizado com sucesso");
    //cria a tabela do sistema (a partir dos modelos ) e se,
    //Nao existirem
    await sequelize.sync({force: true});
  } catch (error) {
    console.error("Erro de conexao com o banco:", error);
  }
}

conecta_db()

app.get("/", (req, res) => {
  res.send("Aula 1: Desenvolvimento de Serviços e APIs");
});

app.listen(port, () => {
  console.log(`Servidor rodando na porta: ${port}`);
});
