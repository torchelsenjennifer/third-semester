import { Router } from "express"
import { excursaoCreate, excursaoIndex } from "./controllers/excursaoController.js"
import { reservaCreate, reservaIndex } from "./controllers/reservaController.js"

const router = Router()

router.get('/excursoes',excursaoIndex)
	  .post('/excursoes', excursaoCreate)

router.get('/reservas', reservaIndex)
	  .post('/reservas', reservaCreate)

export default router