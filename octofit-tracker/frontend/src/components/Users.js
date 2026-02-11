import React, { useState, useEffect } from 'react';

function Users() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [apiUrl, setApiUrl] = useState('');

  useEffect(() => {
    const codespaceName = process.env.REACT_APP_CODESPACE_NAME;
    const url = codespaceName
      ? `https://${codespaceName}-8000.app.github.dev/api/users/`
      : 'http://localhost:8000/api/users/';
    setApiUrl(url);
    console.log('Users Component - Fetching from:', url);

    fetch(url)
      .then((response) => {
        console.log('Users Component - Response status:', response.status);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log('Users Component - Fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const usersData = data.results || data;
        console.log('Users Component - Processed users:', usersData);
        setUsers(Array.isArray(usersData) ? usersData : []);
        setLoading(false);
      })
      .catch((error) => {
        console.error('Users Component - Error fetching users:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="container content-wrapper"><div className="loading-spinner"><div className="spinner-border" role="status"><span className="visually-hidden">Loading...</span></div><p className="mt-3">Loading users...</p></div></div>;
  if (error) return <div className="container content-wrapper"><div className="error-message"><strong>Error:</strong> {error}</div></div>;

  return (
    <div className="container content-wrapper">
      <div className="component-card">
        <div className="card-header-custom">
          <h2>👤 User Profiles</h2>
          <span className="badge bg-light text-dark mt-2">{apiUrl}</span>
        </div>
        <div className="card-body p-0">
          {users.length === 0 ? (
            <div className="empty-state">
              <p>No user profiles found. Register to join!</p>
            </div>
          ) : (
            <div className="table-container">
              <table className="table table-hover mb-0">
                <thead>
                  <tr>
                    <th>ID</th>
                    <th>Username</th>
                    <th>Email</th>
                    <th>Team</th>
                    <th>Joined</th>
                  </tr>
                </thead>
                <tbody>
                  {users.map((user) => (
                    <tr key={user.id}>
                      <td><span className="badge bg-primary">{user.id}</span></td>
                      <td><strong>{user.username}</strong></td>
                      <td>{user.email}</td>
                      <td><span className="badge bg-secondary">{user.team_id}</span></td>
                      <td>{new Date(user.created_at).toLocaleDateString()}</td>
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

export default Users;
