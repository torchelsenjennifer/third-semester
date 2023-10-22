import { DataTypes } from 'sequelize';
import { sequelize } from '../databases/conecta.js';
import { Usuario } from './Usuario.js';

export const Carro = sequelize.define('carro', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true
  },
  modelo: {
    type: DataTypes.STRING(30),
    allowNull: false
  },
  marca: {
    type: DataTypes.STRING(20),
    allowNull: false
  },
  ano: {
    type: DataTypes.INTEGER,
    allowNull: false
  },
  preco: {
    type: DataTypes.DECIMAL(10,2),
    allowNull: false
  }
});

Carro.belongsTo(Usuario, {
	foreignKey: {
	  name: "usuario_id",
	  allowNull: false,
	},
	  onDelete: "RESTRICT",
	  onUpdate: "CASCADE",
  });

Usuario.hasMany(Carro,{
	foreignKey: 'usuario_id'
})