import { DataTypes } from "sequelize";
import { sequelize } from "../databases/conecta.js";
import { Destino } from "./Destino.js";
//para esse destino sairá essa excursao
export const Excursao = sequelize.define("excursao", {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  dataPartida: {
    type: DataTypes.DATE,
    allowNull: false,
  },
  preco: {
    type: DataTypes.DECIMAL(9,2),
    allowNull: false,
  },
  quant_lugares: {
    type: DataTypes.INTEGER(4),
    allowNull: false,
  },
  lugares_reservados: {
    type: DataTypes.INTEGER(4),
    defaultValue:0
  }
},{
	tableName: "excusoes"
  });

// uma excursao pertence a um destino
Excursao.belongsTo(Destino, {
	foreignKey: {
	  name: "destino_id",
	  allowNull: false,
	},
	onDelete: "RESTRICT",
	onUpdate: "CASCADE",
  });
// um destino pode ir a muitas excursoes
Destino.hasMany(Excursao, {
	foreignKey: "destino_id",
  });