const express = require('express');
const users_gen = require('../db/users');

const router = express.Router();

router.get('/', (req, res) => {
  const { limit, offset } = req.query;
  res.json(users_gen(limit, offset));
});

module.exports = router;
