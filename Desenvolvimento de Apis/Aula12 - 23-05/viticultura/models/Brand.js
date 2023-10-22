import { DataTypes } from "sequelize";
import { sequelize } from "../databases/conecta.js";

export const Brand = sequelize.define(
  "brand",
  {
    id: {
      type: DataTypes.INTEGER,
      primaryKey: true,
      autoIncrement: true,
    },
    nome: {
      type: DataTypes.STRING(30),
      allowNull: false,
    },
    cidade: {
      type: DataTypes.STRING(30),
      allowNull: false,
    },
});
