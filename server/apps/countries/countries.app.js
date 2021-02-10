'use strict';

const express = require('express');

const app = express();

app.use('/', require('./countries.routes'));

module.exports = app;
