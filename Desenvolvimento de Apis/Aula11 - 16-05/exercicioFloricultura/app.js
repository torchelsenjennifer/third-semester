import express from 'express'
import cors from "cors"
import routes from './routes.js'
import { sequelize } from './databases/conecta.js'
import { Cliente } from './models/Cliente.js'
import { Produto } from './models/Produto.js'
import { Venda } from './models/venda.js'
import { VendaProposta } from './models/VendaProduto.js'

const app = express()
const port = 3000

app.use(express.json())
app.use(cors())
app.use(routes)

async function conecta_db(){
    try{
        await sequelize.authenticate();
        console.log('Conexão com Banco de dados Realizada com sucesso');
		await Cliente.sync()
		await Produto.sync()
		await Venda.sync()
		await VendaProposta.sync()
    } catch(erro){
        console.error('Erro na conexão com o banco')
    }
}

conecta_db()

app.get('/', (req, res) => {
  res.send('API Floricultura')
})

app.listen(port, () => {
  console.log(`Rodando na porta: ${port}`)
  })