'use strict';

const express = require('express');
const { wrap } = require('@awaitjs/express');
const router = express.Router();

const Countries = require('./countries.controller');

router.route('/').post(wrap(Countries.create));

router.route('/').get(wrap(Countries.list));

router
    .route('/:id([0-9]{0,10})')
    .get(wrap(Countries.find))
    .put(wrap(Countries.update))
    .delete(wrap(Countries.delete));

module.exports = router;
