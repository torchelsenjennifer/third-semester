import { Sequelize } from 'sequelize';

export const sequelize = new Sequelize(
  "restaurantes", "root", "", {
  dialect: "mysql",
  host: "localhost",
  port: 3306
});