import { DataTypes } from 'sequelize';
import { sequelize } from '../databases/conecta.js';

export const Cliente = sequelize.define('cliente', {
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
  endereco: {
    type: DataTypes.STRING(30),
    allowNull: false
  }
});
