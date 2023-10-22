import { DataTypes } from "sequelize";
import { sequelize } from "../databases/conecta.js";
import { Brand } from "./Brand.js";

export const Wine = sequelize.define("wine", {
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
    type: DataTypes.DECIMAL(9, 2),
    allowNull: false,
  },
});

//Um VINHO pertece a uma MARCA - belongsTo
Wine.belongsTo(Brand, {
  foreignKey: {
    name: "marca_id",
    allowNull: false,
    onDelete: "RESTRICT",
    onUpdate: "CASCADE",
  },
});

//Uma Marca te muitoS VINHOS - hasMany
Brand.hasMany(Wine, {
  foreignKey: "marca_id",
});
