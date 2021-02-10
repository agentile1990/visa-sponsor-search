'use strict';

const _ = require('lodash');
const { cities: City } = require('../../sequelize');

class CitiesController {
    static async create(req, res) {
        const body = _.omit(req.body, 'id', 'createdAt', 'updatedAt');

        const city = await City.create(body);

        req.params.id = city.id;

        return CitiesController.find(req, res);
    }

    static async list(req, res) {
        const cities = await City.findAll();

        return res.send(cities);
    }

    static async find(req, res) {
        const city = await City.findByPk(req.params.id);

        if (!city) {
            return res.status(404).send({
                message: `Could not find city with id ${req.params.id}`,
            });
        }

        return res.send({ city });
    }

    static async update(req, res) {
        const body = _.omit(req.body, ['id', 'createdAt', 'updatedAt']);

        const updated = await City.update(body, {
            where: { id: req.params.id },
        });

        if (!updated) {
            return res.status(404).send({
                message: `Could not find city with id ${req.params.id}`,
            });
        }

        return CitiesController.find(req, res);
    }

    static async delete(req, res) {
        const deleted = await City.destroy({ where: { id: req.params.id } });

        if (!deleted) {
            return res.status(404).send({
                message: `Could not find city with id ${req.params.id}`,
            });
        }

        res.status(200).send({});
    }
}

module.exports = CitiesController;
