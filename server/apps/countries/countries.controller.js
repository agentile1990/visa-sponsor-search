'use strict';

const _ = require('lodash');
const { countries: Country } = require('../../sequelize');

class CountriesController {
    static async create(req, res) {
        const body = _.omit(req.body, 'id', 'createdAt', 'updatedAt');

        const country = await Country.create(body);

        req.params.id = country.id;

        return CountriesController.find(req, res);
    }

    static async list(req, res) {
        const countries = await Country.findAll();

        return res.send(countries);
    }

    static async find(req, res) {
        const country = await Country.findByPk(req.params.id);

        if (!country) {
            return res.status(404).send({
                message: `Could not find country with id ${req.params.id}`,
            });
        }

        return res.send({ country });
    }

    static async update(req, res) {
        const body = _.omit(req.body, ['id', 'createdAt', 'updatedAt']);

        const updated = await Country.update(body, {
            where: { id: req.params.id },
        });

        if (!updated) {
            return res.status(404).send({
                message: `Could not find country with id ${req.params.id}`,
            });
        }

        return CountriesController.find(req, res);
    }

    static async delete(req, res) {
        const deleted = await Country.destroy({ where: { id: req.params.id } });

        if (!deleted) {
            return res.status(404).send({
                message: `Could not find country with id ${req.params.id}`,
            });
        }

        res.status(200).send({});
    }
}

module.exports = CountriesController;
