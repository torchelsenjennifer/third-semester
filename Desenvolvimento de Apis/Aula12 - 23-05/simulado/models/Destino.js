import { DataTypes } from "sequelize";
import { sequelize } from "../databases/conecta.js";
//para esse destino sairá essa excursao
export const Destino = sequelize.define("destino", {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  descricao: {
    type: DataTypes.STRING(60),
    allowNull: false,
  },
  roteiro: {
    type: DataTypes.STRING(255),
    allowNull: false,
  },
  tipo_passagem: {
    type: DataTypes.STRING(20),
    allowNull: false,
  },
  dias_duracao: {
    type: DataTypes.INTEGER(3),
    allowNull: false,
  },
  preco: {
    type: DataTypes.DECIMAL(9,2),
    allowNull: false,
  }
});
