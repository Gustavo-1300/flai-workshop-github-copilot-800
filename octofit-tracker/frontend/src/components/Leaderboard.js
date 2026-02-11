import React, { useState, useEffect } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
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
    const apiUrl = `${getApiBaseUrl()}/api/leaderboard/`;
    console.log('Leaderboard Component - Fetching from:', apiUrl);

    fetch(apiUrl)
      .then((response) => {
        console.log('Leaderboard Component - Response status:', response.status);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log('Leaderboard Component - Fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        console.log('Leaderboard Component - Processed leaderboard:', leaderboardData);
        setLeaderboard(Array.isArray(leaderboardData) ? leaderboardData : []);
        setLoading(false);
      })
      .catch((error) => {
        console.error('Leaderboard Component - Error fetching leaderboard:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="container content-wrapper"><div className="loading-spinner"><div className="spinner-border" role="status"><span className="visually-hidden">Loading...</span></div><p className="mt-3">Loading leaderboard...</p></div></div>;
  if (error) return <div className="container content-wrapper"><div className="error-message"><strong>Error:</strong> {error}</div></div>;

  return (
    <div className="container content-wrapper">
      <div className="component-card">
        <div className="card-header-custom">
          <h2>🏆 Leaderboard</h2>
          <span className="badge bg-light text-dark mt-2">{getApiBaseUrl()}/api/leaderboard/</span>
        </div>
        <div className="card-body p-0">
          {leaderboard.length === 0 ? (
            <div className="empty-state">
              <p>No leaderboard data found. Start competing!</p>
            </div>
          ) : (
            <div className="table-container">
              <table className="table table-hover mb-0">
                <thead>
                  <tr>
                    <th>Rank</th>
                    <th>User</th>
                    <th>Team</th>
                    <th>Total Points</th>
                    <th>Activities</th>
                  </tr>
                </thead>
                <tbody>
                  {leaderboard.map((entry, index) => (
                    <tr key={entry.id}>
                      <td>
                        {index === 0 && <span className="badge bg-warning text-dark">🥇 {index + 1}</span>}
                        {index === 1 && <span className="badge bg-secondary">🥈 {index + 1}</span>}
                        {index === 2 && <span className="badge" style={{backgroundColor: '#CD7F32', color: 'white'}}>🥉 {index + 1}</span>}
                        {index > 2 && <span className="badge bg-primary">{index + 1}</span>}
                      </td>
                      <td><strong>{entry.user_id}</strong></td>
                      <td>{entry.team_id}</td>
                      <td><span className="badge bg-success">{entry.total_points} pts</span></td>
                      <td>{entry.activities_completed}</td>
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

export default Leaderboard;
