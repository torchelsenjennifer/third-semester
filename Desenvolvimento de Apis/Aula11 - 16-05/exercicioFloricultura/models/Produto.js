import { DataTypes } from 'sequelize';
import { sequelize } from '../databases/conecta.js';

export const Produto = sequelize.define('produto', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true
  },
  nome: {
    type: DataTypes.STRING(40),
    allowNull: false
  },
  tipo: {
    type: DataTypes.STRING(10),
    allowNull: false
  },
  quantidade: {
	//unisigned: impede que o valor seja negativo
    type: DataTypes.INTEGER(4),
    allowNull: false
  },
  preco: {
    type: DataTypes.DECIMAL(9,2),
    allowNull: false
  }
});
