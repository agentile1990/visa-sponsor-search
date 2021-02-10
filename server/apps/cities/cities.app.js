'use strict';

const express = require('express');

const app = express();

app.use('/', require('./cities.routes'));

module.exports = app;
