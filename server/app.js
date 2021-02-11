require('dotenv').config();
const express = require('express');
const cookieParser = require('cookie-parser');
const logger = require('morgan');

const app = express();

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());

app.use('/countries', require('./apps/countries/countries.app'));
app.use('/cities', require('./apps/cities/cities.app'));
app.use('/companies', require('./apps/companies/companies.app'));
app.use('/sponsorships', require('./apps/sponsorships/sponsorships.app'));

app.use('/*', function (req, res) {
    return res.status(404).send({ message: 'Not Found' });
});

app.use(function (error, req, res, next) {
    console.error('Unhandled Error:', error);
    return res.status(500).send({ message: 'Internal Server Error' });
});

module.exports = app;
