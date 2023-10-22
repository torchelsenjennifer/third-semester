import { Router } from "express"
import { vendaCreate, vendaIndex } from "./controllers/vendaController.js"
import { vendaProdutoCreate, vendaProdutoIndex } from "./controllers/vendaProdutoController.js"

const router = Router()

router.get('/vendas', vendaIndex)
      .post('/vendas', vendaCreate)

router.get('/venda_produtos/:id', vendaProdutoIndex)
      .post('/venda_produtos', vendaProdutoCreate)


export default router