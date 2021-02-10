'use strict';

const express = require('express');
const { wrap } = require('@awaitjs/express');
const router = express.Router();

const Companies = require('./companies.controller');

router.route('/').post(wrap(Companies.create));

router.route('/').get(wrap(Companies.list));

router
    .route('/:id([a-fA-F0-9-]{36})')
    .get(wrap(Companies.find))
    .put(wrap(Companies.update))
    .delete(wrap(Companies.delete));

module.exports = router;
