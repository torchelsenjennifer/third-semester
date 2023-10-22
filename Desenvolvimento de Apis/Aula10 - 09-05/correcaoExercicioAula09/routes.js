import { Router } from "express"
import { propostaCreate, propostaIndex } from "./controllers/propostaController.js"

const router = Router()

router.get('/proposta', propostaIndex)
	  .post('/proposta', propostaCreate)

export default router