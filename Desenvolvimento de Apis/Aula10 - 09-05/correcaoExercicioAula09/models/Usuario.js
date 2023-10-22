import { DataTypes } from 'sequelize';
import { sequelize } from '../databases/conecta.js';

export const Usuario = sequelize.define('usuario', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true
  },
  nome: {
    type: DataTypes.STRING(30),
    allowNull: false
  },
  celular: {
    type: DataTypes.STRING(30),
    allowNull: false
  },
  cargo: {
    type: DataTypes.STRING(30),
    allowNull: false
  }
});