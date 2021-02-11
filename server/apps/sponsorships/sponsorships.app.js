'use strict';

const express = require('express');

const app = express();

app.use('/', require('./sponsorships.routes'));

module.exports = app;
