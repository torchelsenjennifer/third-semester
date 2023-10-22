import { Router } from "express"
import { marcaIndex, marcaCreate, pesquisaMarca, nomedGrupos} from "./controllers/brandController.js"
import { pesquisaVinho, tipodGrupos, vinhoCreate, vinhoIndex } from "./controllers/wineController.js"

const router = Router()

router.get('/brand',marcaIndex)
 	  .post('/brand',marcaCreate )
	  .get('/brand/pesqNome/:pesqMarca', pesquisaMarca )
	  .get('/brand/agrupar/nome', nomedGrupos)

router.get('/wine', vinhoIndex )
	  .post('/wine', vinhoCreate )
	  .get('/wine/pesq/:pesqTipo', pesquisaVinho )
	  .get('/wine/agrupar/tipo', tipodGrupos)


export default router