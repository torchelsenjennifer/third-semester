import express from 'express'
import { sequelize } from './databases/conecta.js'
import cors from "cors"
import routes from './routes.js'
import { Usuario } from './models/Usuario.js'
import { Carro } from './models/Carro.js'
import { Cliente } from './models/Cliente.js'
import { Proposta } from './models/Proposta.js'

const app = express()
const port = 3000

app.use(express.json())
app.use(cors())
app.use(routes)

async function conecta_db(){
    try{
        await sequelize.authenticate();
        console.log('Conex�o com Banco de dados Realizada com sucesso');
		//Pode-se indicar a suncroniza��o das models uma por uma
		await Usuario.sync()
		await Carro.sync()
		await Cliente.sync()
		await Proposta.sync()
//      await sequelize.sync({
// })
    } catch(erro){
        console.error('Erro na conex�o com o banco')
    }
}

conecta_db()

app.get('/', (req, res) => {
  res.send('API Revenda')
})

app.listen(port, () => {
  console.log(`Rodando na porta: ${port}`)
  })