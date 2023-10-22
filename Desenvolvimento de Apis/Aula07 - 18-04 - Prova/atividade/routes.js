import { Router } from "express"
import { cardapioCreate, cardapioDestroy, cardapioIndex, cardapioPrato, cardapioPreco, cardapioUpdate, cardapiodGrupos, cresenteCaloria, mediaCategoria, mediaEstatistica } from "./controllers/cardapioController.js"

const router = Router()

router.get('/cardapios', cardapioIndex)
	  .post('/cardapios', cardapioCreate)
	  .put('/cardapios/:id', cardapioUpdate)
	  .delete('/cardapios/:id', cardapioDestroy)
	  .get('/cardapios/pesq/prato/:prato', cardapioPrato)
	  .get('/cardapio/pesq/preco/:preco', cardapioPreco)
	  .get('/cardapios/cres', cresenteCaloria)
	  .get('/cardapios/estatistica/pratos', mediaEstatistica)
	  .get('/cardapios/estatistica/pesq/categoria/:pesquisa', mediaCategoria)
	  .get('/cardapios/agrupar/categoria',cardapiodGrupos)


export default router