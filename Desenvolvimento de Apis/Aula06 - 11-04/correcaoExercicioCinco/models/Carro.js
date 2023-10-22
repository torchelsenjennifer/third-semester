import { DataTypes } from 'sequelize';
import { sequelize } from '../databases/conecta.js';

export const Carro = sequelize.define('Carro', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true
  },
  modelo: {
    type: DataTypes.STRING(50),
    allowNull: false
  },
  marca: {
    type: DataTypes.STRING(30),
    allowNull: false,
    set(value) {
      this.setDataValue('marca', value.toUpperCase())
    } 
  },
  ano: {
    type: DataTypes.INTEGER(4),
    allowNull: false,
    validate: {
      isInt: true,
//      len: [4, 4],
      len: { 
        args: [4,4],
        msg: "Ano deve possuir 4 digitos"
      },  
      max: {
        args: new Date().getFullYear(),
        msg: "Ano não pode ser maior que o ano atual"
      }  
    }
  },
  preco: {
    type: DataTypes.REAL,
    allowNull: false
  },
  placa: {
    type: DataTypes.STRING(7),
    allowNull: false,
    unique: true,
    validate: {
      verificaTamanho(value) {
        if (value.length != 7) {
          throw new Error('Placa deve possuir 7 caracteres')
        }
      }      
    }
  },
  status: {
    type: DataTypes.VIRTUAL,
    get() {
      const anoAtual = new Date().getFullYear()
      let valor 
      if (this.ano == anoAtual) {
        valor = "Novo"
      } else if (this.ano == anoAtual-1 || this.ano == anoAtual-2) {
        valor = "Semi-novo"
      } else {
        valor = "Usado"
      }
      return valor
    },
    set(value) {
      throw new Error("Erro... o campo status é calculado, não deve ter atribuição")
    }
  }
}, {
  //
});