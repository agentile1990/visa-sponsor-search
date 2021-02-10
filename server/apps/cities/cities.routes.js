'use strict';

const express = require('express');
const { wrap } = require('@awaitjs/express');
const router = express.Router();

const Cities = require('./cities.controller');

router.route('/').post(wrap(Cities.create));

router.route('/').get(wrap(Cities.list));

router
    .route('/:id([a-fA-F0-9-]{36})')
    .get(wrap(Cities.find))
    .put(wrap(Cities.update))
    .delete(wrap(Cities.delete));

module.exports = router;
