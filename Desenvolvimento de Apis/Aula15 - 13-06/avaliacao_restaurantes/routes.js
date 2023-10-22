import { Router } from "express"
import { usuarioCreate, usuarioIndex } from "./controllers/usuarioController.js"
import { avaliacaoCreate, avaliacaoDestroy, avaliacaoIndex } from "./controllers/avaliacaoController.js"

const router = Router()

router.get('/usuarios', usuarioIndex)
      .post('/usuarios', usuarioCreate)

router.get('/avaliacoes', avaliacaoIndex)
      .post('/avaliacoes', avaliacaoCreate)
      .delete('/avaliacoes/:id', avaliacaoDestroy)

export default router