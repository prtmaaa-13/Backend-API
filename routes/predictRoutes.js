const express = require('express');
const router = express.Router();
const { predictAnxiety } = require('../controllers/predictController');

router.post('/predict', predictAnxiety);

module.exports = router;
