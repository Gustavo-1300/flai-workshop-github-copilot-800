import React, { useState, useEffect } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Get API base URL based on environment
  const getApiBaseUrl = () => {
    const codespaceName = process.env.REACT_APP_CODESPACE_NAME;
    if (codespaceName) {
      return `https://${codespaceName}-8000.app.github.dev`;
    }
    return 'http://localhost:8000';
  };

  useEffect(() => {
    const apiUrl = `${getApiBaseUrl()}/api/teams/`;
    console.log('Teams Component - Fetching from:', apiUrl);

    fetch(apiUrl)
      .then((response) => {
        console.log('Teams Component - Response status:', response.status);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log('Teams Component - Fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const teamsData = data.results || data;
        console.log('Teams Component - Processed teams:', teamsData);
        setTeams(Array.isArray(teamsData) ? teamsData : []);
        setLoading(false);
      })
      .catch((error) => {
        console.error('Teams Component - Error fetching teams:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="container content-wrapper"><div className="loading-spinner"><div className="spinner-border" role="status"><span className="visually-hidden">Loading...</span></div><p className="mt-3">Loading teams...</p></div></div>;
  if (error) return <div className="container content-wrapper"><div className="error-message"><strong>Error:</strong> {error}</div></div>;

  return (
    <div className="container content-wrapper">
      <div className="component-card">
        <div className="card-header-custom">
          <h2>👥 Teams</h2>
          <span className="badge bg-light text-dark mt-2">{getApiBaseUrl()}/api/teams/</span>
        </div>
        <div className="card-body p-0">
          {teams.length === 0 ? (
            <div className="empty-state">
              <p>No teams found. Create a team to get started!</p>
            </div>
          ) : (
            <div className="table-container">
              <table className="table table-hover mb-0">
                <thead>
                  <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Description</th>
                    <th>Members</th>
                    <th>Created</th>
                  </tr>
                </thead>
                <tbody>
                  {teams.map((team) => (
                    <tr key={team.id}>
                      <td><span className="badge bg-primary">{team.id}</span></td>
                      <td><strong>{team.name}</strong></td>
                      <td>{team.description}</td>
                      <td><span className="badge bg-info text-dark">{team.members ? team.members.length : 0} members</span></td>
                      <td>{new Date(team.created_at).toLocaleDateString()}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default Teams;
