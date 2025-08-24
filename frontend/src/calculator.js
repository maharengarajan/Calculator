import React, { useState, useEffect } from 'react';

const Calculator = () => {
  const [input, setInput] = useState('');
  const [result, setResult] = useState('');
  const [error, setError] = useState('');
  const [operations, setOperations] = useState([]);

  useEffect(() => {
    // Fetch supported operations from backend
    fetch('/api/operations')
      .then(response => response.json())
      .then(data => setOperations(data))
      .catch(err => console.error('Error fetching operations:', err));
  }, []);

  const handleButtonClick = (value) => {
    setInput(prev => prev + value);
    setError('');
  };

  const handleClear = () => {
    setInput('');
    setResult('');
    setError('');
  };

  const handleCalculate = async () => {
    if (!input) return;
    
    try {
      const response = await fetch('/api/calculate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ expression: input }),
      });
      
      const data = await response.json();
      
      if (response.ok) {
        setResult(data.result);
        setError('');
      } else {
        setError(data.error);
        setResult('');
      }
    } catch (err) {
      setError('Failed to connect to the server');
      setResult('');
    }
  };

  const handleInputChange = (e) => {
    setInput(e.target.value);
    setError('');
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleCalculate();
    }
  };

  return (
    <div className="calculator">
      <div className="calculator-display">
        <input
          type="text"
          value={input}
          onChange={handleInputChange}
          onKeyPress={handleKeyPress}
          className="calculator-input"
          placeholder="Enter expression"
        />
        {result && <div className="calculator-result">Result: {result}</div>}
        {error && <div className="calculator-error">Error: {error}</div>}
      </div>
      
      <div className="calculator-buttons">
        <button onClick={() => handleButtonClick('7')} className="calculator-button">7</button>
        <button onClick={() => handleButtonClick('8')} className="calculator-button">8</button>
        <button onClick={() => handleButtonClick('9')} className="calculator-button">9</button>
        <button onClick={() => handleButtonClick('+')} className="calculator-button operator">+</button>
        
        <button onClick={() => handleButtonClick('4')} className="calculator-button">4</button>
        <button onClick={() => handleButtonClick('5')} className="calculator-button">5</button>
        <button onClick={() => handleButtonClick('6')} className="calculator-button">6</button>
        <button onClick={() => handleButtonClick('-')} className="calculator-button operator">-</button>
        
        <button onClick={() => handleButtonClick('1')} className="calculator-button">1</button>
        <button onClick={() => handleButtonClick('2')} className="calculator-button">2</button>
        <button onClick={() => handleButtonClick('3')} className="calculator-button">3</button>
        <button onClick={() => handleButtonClick('*')} className="calculator-button operator">*</button>
        
        <button onClick={() => handleButtonClick('0')} className="calculator-button">0</button>
        <button onClick={() => handleButtonClick('.')} className="calculator-button">.</button>
        <button onClick={() => handleButtonClick('/')} className="calculator-button operator">/</button>
        <button onClick={() => handleButtonClick('**')} className="calculator-button operator">^</button>
        
        <button onClick={() => handleButtonClick('(')} className="calculator-button">(</button>
        <button onClick={() => handleButtonClick(')')} className="calculator-button">)</button>
        <button onClick={handleClear} className="calculator-button clear">C</button>
        <button onClick={handleCalculate} className="calculator-button equals">=</button>
      </div>
      
      <div className="operations-list">
        <h3>Supported Operations</h3>
        <ul>
          {operations.map((op, index) => (
            <li key={index}>
              <strong>{op.name}</strong>: {op.example}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Calculator;