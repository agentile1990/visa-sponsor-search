'use strict';

const express = require('express');

const app = express();

app.use('/', require('./companies.routes'));

module.exports = app;
