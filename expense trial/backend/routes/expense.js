const express = require('express');
const router = express.Router();

let expenses = [];  // Sample in-memory data

// GET all expenses
router.get('/', (req, res) => {
  res.json(expenses);
});

// POST a new expense
router.post('/', (req, res) => {
  const expense = {
    id: expenses.length + 1,
    description: req.body.description,
    amount: req.body.amount,
    date: req.body.date || new Date().toISOString().split('T')[0]
  };
  expenses.push(expense);
  res.status(201).json(expense);
});

// PUT update an expense
router.put('/:id', (req, res) => {
  const { id } = req.params;
  const { description, amount } = req.body;
  const expense = expenses.find(e => e.id == id);

  if (expense) {
    expense.description = description;
    expense.amount = amount;
    res.json(expense);
  } else {
    res.status(404).json({ message: 'Expense not found' });
  }
});

// DELETE an expense
router.delete('/:id', (req, res) => {
  const { id } = req.params;
  expenses = expenses.filter(e => e.id != id);
  res.status(204).send();
});

module.exports = router;
