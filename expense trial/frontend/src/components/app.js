import React, { useState, useEffect } from 'react';
import axios from 'axios';
import ExpenseList from './ExpenseList';

const App = () => {
  const [expenses, setExpenses] = useState([]);
  const [description, setDescription] = useState('');
  const [amount, setAmount] = useState('');

  useEffect(() => {
    fetchExpenses();
  }, []);

  const fetchExpenses = async () => {
    const res = await axios.get('http://localhost:5000/api/expenses');
    setExpenses(res.data);
  };

  const addExpense = async () => {
    const newExpense = { description, amount: parseFloat(amount) };
    const res = await axios.post('http://localhost:5000/api/expenses', newExpense);
    setExpenses([...expenses, res.data]);
    setDescription('');
    setAmount('');
  };

  return (
    <div>
      <h1>Expense Tracker</h1>
      <input
        type="text"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        placeholder="Expense Description"
      />
      <input
        type="number"
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
        placeholder="Amount"
      />
      <button onClick={addExpense}>Add Expense</button>
      
      <ExpenseList expenses={expenses} />
    </div>
  );
};

export default App;
