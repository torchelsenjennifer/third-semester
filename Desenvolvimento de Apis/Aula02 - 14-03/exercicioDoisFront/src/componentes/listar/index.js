import { useState, useEffect } from "react";
import axios from "axios";

export default function App() {
  const [lista, setLista] = useState([]);

  async function buscaProdutos() {
    const dados = await axios.get("http://localhost:3000/produtos");
    setLista(dados.data);
  }

  // chama o método ao carregar o componente
  useEffect(() => {
    buscaProdutos();
  }, []);

  const prods = lista.map((l) => (
    <tr key={l.id}>
      <td>{l.id}</td>
      <td>{l.descricao}</td>
      <td>{l.marca}</td>
      <td className="text-center">{l.quant}</td>
      <td className="text-center">
        {l.preco.toLocaleString("pt-br", { minimumFractionDigits: 2 })}
      </td>
    </tr>
  ));

  return (
    <div className="container">
      <nav className="navbar bg-primary" data-bs-theme="dark">
        <h3 className="fst-italic mx-3">Lista de Produtos</h3>
      </nav>

      <table className="table table-striped">
        <thead>
          <tr>
            <th>Código</th>
            <th>Descrição</th>
            <th>Marca</th>
            <th>Quant.</th>
            <th>Preço R$</th>
          </tr>
        </thead>
        <tbody>{prods}</tbody>
      </table>
    </div>
  );
}