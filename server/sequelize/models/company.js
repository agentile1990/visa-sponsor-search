const { Model, Sequelize } = require('sequelize');
module.exports = (sequelize, DataTypes) => {
    class Company extends Model {}
    Company.init(
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
            cityId: {
                type: DataTypes.UUID,
                allowNull: false,
            },
        },
        { sequelize, modelName: 'companies' },
    );
    return Company;
};
