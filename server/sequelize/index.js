'use strict';

const fs = require('fs');
const path = require('path');
const Sequelize = require('sequelize');

const config = require('./config')[process.env.NODE_ENV || 'development'];

class Db {
    constructor() {
        if (!Db.instance) {
            const db = {};

            const sequelize = new Sequelize(
                config.database,
                config.username,
                config.password,
                config,
            );

            const modelsPath = path.join(__dirname, './models');
            fs.readdirSync(modelsPath).forEach((file) => {
                const model = require(path.join(modelsPath, file))(
                    sequelize,
                    Sequelize.DataTypes,
                );
                db[model.name] = model;
            });

            Object.keys(db).forEach((modelName) => {
                if (db[modelName].associate) {
                    db[modelName].associate(db);
                }
            });

            db.sequelize = sequelize;

            Db.instance = db;
        }

        return Db.instance;
    }
}

const instance = new Db();

module.exports = instance;
