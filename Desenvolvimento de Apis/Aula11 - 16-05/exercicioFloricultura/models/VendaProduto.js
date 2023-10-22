import { DataTypes } from "sequelize";
import { sequelize } from "../databases/conecta.js";
import { Produto } from "./Produto.js";
import { Venda } from "./venda.js";

export const VendaProposta = sequelize.define(
  "vendaproduto",
  {
    id: {
      type: DataTypes.INTEGER,
      primaryKey: true,
      autoIncrement: true,
    },
    quant: {
      type: DataTypes.INTEGER(4),
      allowNull: false,
    },
    preco: {
      type: DataTypes.DECIMAL(9,2),
      allowNull: false,
    },
  },
  {
    tableName: "venda_protudos",
  }
);

VendaProposta.belongsTo(Venda, {
  foreignKey: {
    name: "venda_id",
    allowNull: false,
  },
  onDelete: "RESTRICT",
  onUpdate: "CASCADE",
});

Venda.hasMany(VendaProposta, {
  foreignKey: "venda_id",
});

VendaProposta.belongsTo(Produto, {
  foreignKey: {
    name: "produto_id",
    allowNull: false,
  },
  onDelete: "RESTRICT",
  onUpdate: "CASCADE",
});

// Produto.hasMany(VendaProposta, {
//   foreignKey: "carro_id",
// });
