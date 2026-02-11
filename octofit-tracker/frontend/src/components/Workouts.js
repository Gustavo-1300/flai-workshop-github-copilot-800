import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [apiUrl, setApiUrl] = useState('');

  useEffect(() => {
    const codespaceName = process.env.REACT_APP_CODESPACE_NAME;
    const url = codespaceName
      ? `https://${codespaceName}-8000.app.github.dev/api/workouts/`
      : 'http://localhost:8000/api/workouts/';
    setApiUrl(url);
    console.log('Workouts Component - Fetching from:', url);

    fetch(url)
      .then((response) => {
        console.log('Workouts Component - Response status:', response.status);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log('Workouts Component - Fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        console.log('Workouts Component - Processed workouts:', workoutsData);
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      })
      .catch((error) => {
        console.error('Workouts Component - Error fetching workouts:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="container content-wrapper"><div className="loading-spinner"><div className="spinner-border" role="status"><span className="visually-hidden">Loading...</span></div><p className="mt-3">Loading workouts...</p></div></div>;
  if (error) return <div className="container content-wrapper"><div className="error-message"><strong>Error:</strong> {error}</div></div>;

  return (
    <div className="container content-wrapper">
      <div className="component-card">
        <div className="card-header-custom">
          <h2>💪 Workouts</h2>
          <span className="badge bg-light text-dark mt-2">{apiUrl}</span>
        </div>
        <div className="card-body p-0">
          {workouts.length === 0 ? (
            <div className="empty-state">
              <p>No workouts found. Check back for personalized suggestions!</p>
            </div>
          ) : (
            <div className="table-container">
              <table className="table table-hover mb-0">
                <thead>
                  <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Type</th>
                    <th>Duration</th>
                    <th>Difficulty</th>
                    <th>Description</th>
                  </tr>
                </thead>
                <tbody>
                  {workouts.map((workout) => (
                    <tr key={workout.id}>
                      <td><span className="badge bg-primary">{workout.id}</span></td>
                      <td><strong>{workout.name}</strong></td>
                      <td><span className="badge bg-info text-dark">{workout.workout_type}</span></td>
                      <td>{workout.duration} min</td>
                      <td>
                        {workout.difficulty_level === 'Easy' && <span className="badge bg-success">{workout.difficulty_level}</span>}
                        {workout.difficulty_level === 'Medium' && <span className="badge bg-warning text-dark">{workout.difficulty_level}</span>}
                        {workout.difficulty_level === 'Hard' && <span className="badge bg-danger">{workout.difficulty_level}</span>}
                        {!['Easy', 'Medium', 'Hard'].includes(workout.difficulty_level) && <span className="badge bg-secondary">{workout.difficulty_level}</span>}
                      </td>
                      <td>{workout.description}</td>
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

export default Workouts;
