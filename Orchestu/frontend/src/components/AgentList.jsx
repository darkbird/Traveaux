import React, { useState, useEffect } from 'react';

function AgentList() {
  const [agents, setAgents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Phase 1: Start with Mock Data
    const mockAgents = [
      { agent_id: 'agent-001-mock', name: 'Mock Agent Alpha', description: 'Agent for testing purposes', status: 'active', config: { type: 'mock' } },
      { agent_id: 'agent-002-mock', name: 'Mock Agent Beta', description: 'Another test agent for the UI', status: 'inactive', config: { type: 'mock' } },
    ];
    setAgents(mockAgents);
    setLoading(false);

    // Phase 1.5 (Attempt if backend is easily accessible by frontend in subtask):
    // console.log("Attempting to fetch agents from backend...");
    // fetch('http://localhost:5000/agents') // Assuming backend runs on 5000
    //   .then(response => {
    //     if (!response.ok) {
    //       console.error('Network response was not ok:', response.status, response.statusText);
    //       throw new Error(`Network response was not ok: ${response.statusText} (status: ${response.status})`);
    //     }
    //     return response.json();
    //   })
    //   .then(data => {
    //     console.log("Fetched data:", data);
    //     // The backend /agents route returns a list directly.
    //     // If it was { "agents": [...] }, then data.agents would be correct.
    //     setAgents(data || []); // Ensure data is an array, use empty if data is null/undefined
    //     setLoading(false);
    //   })
    //   .catch(error => {
    //     console.error("Failed to fetch agents, using mock data as fallback:", error);
    //     setError(error.message); // Set error state to display message
    //     // setLoading(false); // Already set mock data, so loading is effectively false.
    //     // No need to set mockAgents again, they are the default.
    //   });
  }, []);

  if (loading) return <p>Loading agents...</p>;
  // If there's an error, show the error message but still proceed to show mock data (or whatever is in 'agents' state)
  // This behavior is because mock data is set initially.
  // If fetch was the *only* source, you might only show error.

  return (
    <div>
      <h2>Agent List</h2>
      {error && <p style={{ color: 'red' }}>Error loading agents from backend: {error}. Displaying mock data instead.</p>}
      {agents.length === 0 && !error ? <p>No agents found.</p> : (
        <ul>
          {agents.map(agent => (
            <li key={agent.agent_id}>
              <strong>{agent.name}</strong> ({agent.agent_id}) - Status: {agent.status}
              <p>{agent.description}</p>
              {/* Displaying config as a string for simplicity */}
              <p><small>Config: {JSON.stringify(agent.config)}</small></p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default AgentList;
