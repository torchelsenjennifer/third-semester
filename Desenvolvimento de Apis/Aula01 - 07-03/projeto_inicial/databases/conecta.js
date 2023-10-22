import { Sequelize } from "sequelize";

// Option 2: Passing parameters separately (sqlite)
export const sequelize = new Sequelize({
  dialect: "sqlite",
  storage: "./databases/estoque.db3"
});
