import { Sequelize } from 'sequelize';

export const sequelize = new Sequelize("turismo","root","",{
  dialect: 'mysql',
  host:"localhost",
  port:3306,
})