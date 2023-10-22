import { DataTypes } from "sequelize";
import { sequelize } from "../databases/conecta.js";
import { Cliente } from "./Cliente.js";
import { Excursao } from "./Excursao.js";

export const Reserva = sequelize.define("reserva", {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  quantComprados: {
    type: DataTypes.INTEGER(4),
    allowNull: false,
  },
   precoTotal: {
    type: DataTypes.DECIMAL(9,2),
    allowNull: false,
  }
},{
	tableName: "reservas"
});

//uma reserva pertence a um cliente
Reserva.belongsTo(Cliente, {
	foreignKey: {
	  name: "cliente_id",
	  allowNull: false,
	},
	onDelete: "RESTRICT",
	onUpdate: "CASCADE",
  });
//um cliente pode fazer varias reservas
Cliente.hasMany(Reserva, {
	foreignKey: "cliente_id",
  });


//Uma reserva pertence a uma excursao
Reserva.belongsTo(Excursao, {
	foreignKey: {
	  name: "excursao_id",
	  allowNull: false,
	},
	onDelete: "RESTRICT",
	onUpdate: "CASCADE",
  });
//uma excursao pode ter varias reservas
Excursao.hasMany(Reserva, {
	foreignKey: "excursao_id",
  });