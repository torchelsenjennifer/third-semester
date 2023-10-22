import { DataTypes } from "sequelize";
import { sequelize } from "../databases/conecta.js";
import { Cliente } from "./Cliente.js";
import { Carro } from "./Carro.js";

export const Proposta = sequelize.define(
  "proposta",
  {
    id: {
      type: DataTypes.INTEGER,
      primaryKey: true,
      autoIncrement: true,
    },
    descricao: {
      type: DataTypes.STRING(255),
      allowNull: false,
    },
    resposta: {
      type: DataTypes.STRING(255),
    },
  },
  {
    tableName: "propostas",
  }
);

Proposta.belongsTo(Cliente, {
  foreignKey: {
    name: "cliente_id",
    allowNull: false,
  },
  onDelete: "RESTRICT",
  onUpdate: "CASCADE",
});

Cliente.hasMany(Proposta, {
  foreignKey: "cliente_id",
});

Proposta.belongsTo(Carro, {
  foreignKey: {
    name: "carro_id",
    allowNull: false,
  },
  onDelete: "RESTRICT",
  onUpdate: "CASCADE",
});

Carro.hasMany(Proposta, {
  foreignKey: "carro_id",
});
