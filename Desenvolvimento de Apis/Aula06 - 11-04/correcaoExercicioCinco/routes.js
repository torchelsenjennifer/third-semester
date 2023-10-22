import { Router } from "express"
import { carroCreate, carroGrupos, carroIndex, carroStatus } from "./controllers/carroController.js"

const router = Router()

router.get('/carros', carroIndex)
      .post('/carros', carroCreate)
      .get('/carros/:valor', carroStatus)
      .get('/carros/agrupar/marca', carroGrupos)
      
export default router