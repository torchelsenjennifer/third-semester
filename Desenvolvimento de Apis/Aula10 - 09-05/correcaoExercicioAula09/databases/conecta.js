import { Sequelize } from 'sequelize';

// export const sequelize = new Sequelize("casa_vinhos","root","1234",{
//   dialect: 'mysql',
//   host:"localhost",
//   port:3306,

// });
export const sequelize = new Sequelize({
	dialect: 'sqlite',
 	storage: './databases/revenda.db'
  });

// CRIAR BANCO DE DADOS COM O NOME REVENDA
//   msql -u root -p
//   create database revenda
