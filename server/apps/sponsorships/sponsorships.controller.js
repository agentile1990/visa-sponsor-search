'use strict';

const _ = require('lodash');
const { sponsorships: Sponsorship } = require('../../sequelize');

class SponsorshipsController {
    static async create(req, res) {
        const body = _.omit(req.body, 'id', 'createdAt', 'updatedAt');

        const sponsorship = await Sponsorship.create(body);

        req.params.id = sponsorship.id;

        return SponsorshipsController.find(req, res);
    }

    static async list(req, res) {
        const sponsorships = await Sponsorship.findAll();

        return res.send(sponsorships);
    }

    static async find(req, res) {
        const sponsorship = await Sponsorship.findByPk(req.params.id);

        if (!sponsorship) {
            return res.status(404).send({
                message: `Could not find sponsorship with id ${req.params.id}`,
            });
        }

        return res.send({ sponsorship });
    }

    static async update(req, res) {
        const body = _.omit(req.body, ['id', 'createdAt', 'updatedAt']);

        const updated = await Sponsorship.update(body, {
            where: { id: req.params.id },
        });

        if (!updated) {
            return res.status(404).send({
                message: `Could not find sponsorship with id ${req.params.id}`,
            });
        }

        return SponsorshipsController.find(req, res);
    }

    static async delete(req, res) {
        const deleted = await Sponsorship.destroy({
            where: { id: req.params.id },
        });

        if (!deleted) {
            return res.status(404).send({
                message: `Could not find sponsorship with id ${req.params.id}`,
            });
        }

        res.status(200).send({});
    }
}

module.exports = SponsorshipsController;
