import { Sequelize } from 'sequelize';

export const sequelize = new Sequelize("viticultura","root","",{
  dialect: 'mysql',
  host:"localhost",
  port:3306,
})