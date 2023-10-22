import { Router } from "express"
import { vendaIndex } from "./controllers/vendaController.js"

const router = Router()

router.get('/venda', vendaIndex)
// 	  .post('/proposta', propostaCreate)

export default router