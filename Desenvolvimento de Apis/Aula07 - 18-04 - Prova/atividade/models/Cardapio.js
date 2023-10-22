import { DataTypes } from 'sequelize';
import { sequelize } from '../databases/conecta.js';

export const Cardapio = sequelize.define('Cardapio', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true
  },
  prato: {
    type: DataTypes.STRING(30),
    allowNull: false
  },
  categoria: {
    type: DataTypes.STRING(40),
    allowNull: false
  },
  preco: {
    type: DataTypes.REAL,
    allowNull: false
  },
  calorias: {
    type: DataTypes.REAL,
    allowNull: false
  },
}, {
  tableName : 'cardapios'
});