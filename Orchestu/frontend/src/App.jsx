import React from 'react';
import './App.css'; // You can create a minimal App.css
import AgentList from './components/AgentList';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Agent Management Dashboard</h1>
      </header>
      <main>
        <AgentList />
      </main>
      <footer>
        <p>Orchestu Agent Platform - Phase 1 Frontend</p>
      </footer>
    </div>
  );
}

export default App;
