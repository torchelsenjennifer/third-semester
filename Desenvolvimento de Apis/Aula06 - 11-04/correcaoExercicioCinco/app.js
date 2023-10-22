import express from 'express'
import { sequelize } from './databases/conecta.js'
import cors from "cors"
import routes from './routes.js'

const app = express()
const port = 3000

app.use(express.json())
app.use(cors())
app.use(routes)

async function conecta_db() {
  try {
    await sequelize.authenticate();
    console.log('Conexão com banco de dados realizada com sucesso');
    await sequelize.sync();  // cria as tabelas do sistema (a partir dos modelos - se não existirem)
//    await sequelize.sync({alter: true});  // atualiza as tabelas conforme a model
  } catch (error) {
    console.error('Erro na conexão com o banco: ', error);
  }
}
conecta_db()

app.get('/', (req, res) => {
  res.send('API de Cadastro de Carros')
})

app.listen(port, () => {
  console.log(`Servidor Rodando na Porta: ${port}`)
})