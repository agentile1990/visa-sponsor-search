const express = require('express');
const router = express.Router();

router.get('/', function (req, res) {
    res.send({ message: 'Hello from visa-sponsor-search API' });
});

module.exports = router;
