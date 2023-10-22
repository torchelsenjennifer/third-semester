import { Router } from "express"
import { marcaCreate, marcaIndex } from "./controllers/marcaController.js"
import { vinhoCreate, vinhoIndex } from "./controllers/vinhoController.js"

const router = Router()

router.get('/marcas', marcaIndex)
	  .post('/marcas', marcaCreate)

router.get('/vinhos', vinhoIndex)
      .post('/vinhos', vinhoCreate)

export default router