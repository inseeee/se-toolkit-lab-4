import React, { useState, useEffect } from 'react';

const API_TOKEN_KEY = 'api_token';
const API_BASE_URL = import.meta.env.VITE_API_TARGET;

interface Item {
  id: number;
  type: string;
  title: string;
  description: string;
  created_at: string;
}

function App() {
  const [token, setToken] = useState(localStorage.getItem(API_TOKEN_KEY) || '');
  const [data, setData] = useState<Item[]>([]);
  const [columns] = useState<string[]>(['id', 'type', 'title', 'description', 'created_at']);
  const [error, setError] = useState('');

  useEffect(() => {
    if (token) {
      fetchData();
    }
  }, [token]);

  const fetchData = async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/items/`, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });
      if (!response.ok) throw new Error('Failed to fetch');
      const result = await response.json();
      setData(result);
    } catch (err) {
      setError('Failed to fetch data');
    }
  };

  const handleConnect = () => {
    localStorage.setItem(API_TOKEN_KEY, token);
    fetchData();
  };

  const handleDisconnect = () => {
    localStorage.removeItem(API_TOKEN_KEY);
    setToken('');
    setData([]);
  };

  if (!token) {
    return (
      <div style={{ padding: '2rem' }}>
        <h1>API Token</h1>
        <p>Enter your API token to connect.</p>
        <input
          type="text"
          value={token}
          onChange={(e) => setToken(e.target.value)}
          placeholder="Token"
          style={{ marginRight: '1rem' }}
        />
        <button onClick={handleConnect}>Connect</button>
      </div>
    );
  }

  return (
    <div style={{ padding: '2rem' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h1>Items</h1>
        <button onClick={handleDisconnect}>Disconnect</button>
      </div>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {data.length > 0 ? (
        <table border={1} cellPadding={8} style={{ borderCollapse: 'collapse', width: '100%' }}>
          <thead>
            <tr>
              {columns.map(col => <th key={col}>{col}</th>)}
            </tr>
          </thead>
          <tbody>
            {data.map((row, i) => (
              <tr key={i}>
                {columns.map(col => <td key={col}>{String(row[col as keyof Item])}</td>)}
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>No data</p>
      )}
    </div>
  );
}

export default App;
