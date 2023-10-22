import { DataTypes } from "sequelize";
import { sequelize } from "../databases/conecta.js";
import { Marca } from "./Marca.js";

export const Vinho = sequelize.define("vinho", {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  tipo: {
    type: DataTypes.STRING(30),
    allowNull: false,
  },
  preco: {
    type: DataTypes.DECIMAL(9, 2),
    allowNull: false,
  },
  teor: {
    type: DataTypes.DECIMAL(4, 1),
    allowNull: false,
  },
});

Vinho.belongsTo(Marca, {
  foreignKey: {
    name: "marca_id",
    allowNull: false,
    onDelete: "RESTRICT",
    onUpdate: "CASCADE",
  },
});

Marca.hasMany(Vinho, {
  foreignKey: "marca_id",
});
