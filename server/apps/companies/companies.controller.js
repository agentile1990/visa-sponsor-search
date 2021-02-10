'use strict';

const _ = require('lodash');
const { companies: Company } = require('../../sequelize');

class CompaniesController {
    static async create(req, res) {
        const body = _.omit(req.body, 'id', 'createdAt', 'updatedAt');

        const company = await Company.create(body);

        req.params.id = company.id;

        return CompaniesController.find(req, res);
    }

    static async list(req, res) {
        const companies = await Company.findAll();

        return res.send(companies);
    }

    static async find(req, res) {
        const company = await Company.findByPk(req.params.id);

        if (!company) {
            return res.status(404).send({
                message: `Could not find company with id ${req.params.id}`,
            });
        }

        return res.send({ company });
    }

    static async update(req, res) {
        const body = _.omit(req.body, ['id', 'createdAt', 'updatedAt']);

        const updated = await Company.update(body, {
            where: { id: req.params.id },
        });

        if (!updated) {
            return res.status(404).send({
                message: `Could not find company with id ${req.params.id}`,
            });
        }

        return CompaniesController.find(req, res);
    }

    static async delete(req, res) {
        const deleted = await Company.destroy({ where: { id: req.params.id } });

        if (!deleted) {
            return res.status(404).send({
                message: `Could not find company with id ${req.params.id}`,
            });
        }

        res.status(200).send({});
    }
}

module.exports = CompaniesController;
