import { Router } from "express";
import { produtoIndex } from "./controllers/produtoController.js";

const router = Router();

router.get("/produtos", produtoIndex);

export default router;
