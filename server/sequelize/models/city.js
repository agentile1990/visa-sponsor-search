const { Model, Sequelize } = require('sequelize');
module.exports = (sequelize, DataTypes) => {
    class City extends Model {}
    City.init(
        {
            id: {
                primaryKey: true,
                type: DataTypes.UUID,
                defaultValue: Sequelize.UUIDV4,
            },
            name: {
                type: DataTypes.TEXT,
                allowNull: false,
                unique: true,
            },
            countryId: {
                type: DataTypes.INTEGER,
                allowNull: false,
            },
        },
        { sequelize, modelName: 'cities' },
    );
    return City;
};
