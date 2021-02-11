'use strict';

const express = require('express');
const { wrap } = require('@awaitjs/express');
const router = express.Router();

const Sponsorships = require('./sponsorships.controller');

router.route('/').post(wrap(Sponsorships.create));

router.route('/').get(wrap(Sponsorships.list));

router
    .route('/:id([a-fA-F0-9-]{36})')
    .get(wrap(Sponsorships.find))
    .put(wrap(Sponsorships.update))
    .delete(wrap(Sponsorships.delete));

module.exports = router;
