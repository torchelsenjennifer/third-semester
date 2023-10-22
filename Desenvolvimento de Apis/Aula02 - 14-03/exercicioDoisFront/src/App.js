import { useState } from "react";
import axios from "axios";


export default function App() {
  const [descricao, setDescricao] = useState("");
  const [marca, setMarca] = useState("");
  const [quant, setQuant] = useState("");
  const [preco, setPreco] = useState("");

  async function enviaDados(e) {
    e.preventDefault();
    const objProduto = {
      descricao,
      marca,
      quant,
      preco
    };
    const produto = await axios.post(
      "http://localhost:3000/",
      objProduto
    );
    console.log(produto);
  }

  return (
    <div className="container-fluid">
      <nav className="navbar bg-primary" data-bs-theme="dark">
        <h3 className="fst-italic mx-3">Inclusão de Produtos</h3>
      </nav>
      <form className="mx-3 mt-3" onSubmit={enviaDados}>
        <div className="form-group">
          <label htmlfor="titulo">Descrição:</label>
          <input
            type="text"
            className="form-control"
            id="titulo"
            required
            value={descricao}
            onChange={(e) => setDescricao(e.target.value)}
          />
        </div>
        <div className="form-group mt-2">
          <label htmlforfor="autor">Marca:</label>
          <input
            type="text"
            className="form-control"
            id="marca"
            required
            value={marca}
            onChange={(e) => setMarca(e.target.value)}
          />
        </div>
        <div className="row mt-2">
          <div className="col-sm-4">
            <div className="form-group">
              <label for="ano">Quantidade:</label>
              <input
                type="number"
                className="form-control"
                id="quant"
                required
                value={quant}
                onChange={(e) => setQuant(e.target.value)}
              />
            </div>
          </div>
          <div className="col-sm-8">
            <div className="form-group">
              <label for="preco">Preço R$:</label>
              <input
                type="number"
                className="form-control"
                id="preco"
                step="0.01"
                required
                value={preco}
                onChange={(e) => setPreco(e.target.value)}
              />
            </div>
          </div>
        </div>
        <input type="submit" className="btn btn-primary my-3" value="Enviar" />
        <input
          type="reset"
          className="btn btn-danger my-3 ms-3"
          value="Limpar"
        />
        <h3> </h3>
      </form>
    </div>
  );
}
