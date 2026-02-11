import React, { useState, useEffect } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [apiUrl, setApiUrl] = useState('');

  useEffect(() => {
    const codespaceName = process.env.REACT_APP_CODESPACE_NAME;
    const url = codespaceName
      ? `https://${codespaceName}-8000.app.github.dev/api/activities/`
      : 'http://localhost:8000/api/activities/';
    setApiUrl(url);
    console.log('Activities Component - Fetching from:', url);

    fetch(url)
      .then((response) => {
        console.log('Activities Component - Response status:', response.status);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log('Activities Component - Fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const activitiesData = data.results || data;
        console.log('Activities Component - Processed activities:', activitiesData);
        setActivities(Array.isArray(activitiesData) ? activitiesData : []);
        setLoading(false);
      })
      .catch((error) => {
        console.error('Activities Component - Error fetching activities:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="container content-wrapper"><div className="loading-spinner"><div className="spinner-border" role="status"><span className="visually-hidden">Loading...</span></div><p className="mt-3">Loading activities...</p></div></div>;
  if (error) return <div className="container content-wrapper"><div className="error-message"><strong>Error:</strong> {error}</div></div>;

  return (
    <div className="container content-wrapper">
      <div className="component-card">
        <div className="card-header-custom">
          <h2>📊 Activities</h2>
          <span className="badge bg-light text-dark mt-2">{apiUrl}</span>
        </div>
        <div className="card-body p-0">
          {activities.length === 0 ? (
            <div className="empty-state">
              <p>No activities found. Start tracking your fitness journey!</p>
            </div>
          ) : (
            <div className="table-container">
              <table className="table table-hover mb-0">
                <thead>
                  <tr>
                    <th>ID</th>
                    <th>User</th>
                    <th>Type</th>
                    <th>Duration</th>
                    <th>Distance</th>
                    <th>Calories</th>
                    <th>Date</th>
                  </tr>
                </thead>
                <tbody>
                  {activities.map((activity) => (
                    <tr key={activity.id}>
                      <td><span className="badge bg-primary">{activity.id}</span></td>
                      <td>{activity.user_id}</td>
                      <td><span className="badge bg-info text-dark">{activity.activity_type}</span></td>
                      <td>{activity.duration} min</td>
                      <td>{activity.distance} km</td>
                      <td><span className="badge bg-success">{activity.calories_burned} cal</span></td>
                      <td>{new Date(activity.date).toLocaleDateString()}</td>
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

export default Activities;
