import { DataTypes } from "sequelize";
import { sequelize } from "../databases/conecta.js";
import { Cliente } from "./Cliente.js";

export const Venda = sequelize.define("venda", {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  data: {
    type: DataTypes.DATE,
    allowNull: false,
  },
  total: {
    type: DataTypes.DECIMAL(9, 2),
    //allowNull: false
    //VAI COMECAR COM UM VALOR
    defaultValue: 0,
  },
});
//pertence - belongsTo
Venda.belongsTo(Cliente, {
  foreignKey: {
    name: "cliente_id",
    allowNull: false,
  },
  onDelete: "RESTRICT",
  onUpdate: "CASCADE",
});
//muitas - hasMany
Cliente.hasMany(Venda, {
  foreignKey: "cliente_id",
});
