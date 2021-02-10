const { Model, Sequelize } = require('sequelize');
module.exports = (sequelize, DataTypes) => {
    class Country extends Model {}
    Country.init(
        {
            id: {
                primaryKey: true,
                type: DataTypes.INTEGER,
                autoIncrement: true,
            },
            name: {
                type: DataTypes.TEXT,
                allowNull: false,
                unique: true,
            },
            code3: {
                type: DataTypes.TEXT,
                allowNull: false,
                unique: true,
            },
        },
        { sequelize, modelName: 'countries' },
    );
    return Country;
};
