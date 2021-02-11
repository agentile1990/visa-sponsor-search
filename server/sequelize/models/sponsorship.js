const { Model, Sequelize } = require('sequelize');
module.exports = (sequelize, DataTypes) => {
    class Sponsorship extends Model {}
    Sponsorship.init(
        {
            id: {
                primaryKey: true,
                type: DataTypes.UUID,
                defaultValue: Sequelize.UUIDV4,
            },
            type: {
                type: DataTypes.TEXT,
            },
            route: {
                type: DataTypes.TEXT,
            },
            countryId: {
                type: DataTypes.INTEGER,
                allowNull: false,
            },
            cityId: {
                type: DataTypes.UUID,
                allowNull: false,
            },
            companyId: {
                type: DataTypes.UUID,
                allowNull: false,
            },
        },
        { sequelize, modelName: 'sponsorships' },
    );
    return Sponsorship;
};
