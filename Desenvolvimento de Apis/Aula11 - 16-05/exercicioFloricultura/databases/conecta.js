import { Sequelize } from 'sequelize';

// export const sequelize = new Sequelize("floricultura","root","",{
//   dialect: 'mysql',
//   host:"localhost",
//   port:3306,
// })

// });
export const sequelize = new Sequelize({
	dialect: 'sqlite',
 	storage: './databases/floricultura.db'
  });

// CRIAR BANCO DE DADOS COM O NOME REVENDA
//   msql -u root -p
//   create database floricultura