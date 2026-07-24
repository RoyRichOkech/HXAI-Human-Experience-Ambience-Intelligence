import React, { useState, useEffect } from 'react';
import '../App.css';

function Context() {
  const [context, setContext] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [device, setDevice] = useState('');
  const [location, setLocation] = useState('');
  const [currentGoal, setCurrentGoal] = useState('');
  const [currentActivity, setCurrentActivity] = useState('');
  const [emotionalState, setEmotionalState] = useState('');

  useEffect(() => {
    fetchContext();
  }, []);

  const fetchContext = async () => {
    setLoading(true);
    try {
      const token = localStorage.getItem('access_token');
      const response = await fetch('http://localhost:8000/api/context/', {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });
      if (response.ok) {
        const data = await response.json();
        setContext(data);
        setDevice(data.device || '');
        setLocation(data.location || '');
        setCurrentGoal(data.current_goal || '');
        setCurrentActivity(data.current_activity || '');
        setEmotionalState(data.emotional_state || '');
      }
    } catch (error) {
      console.error('Error fetching context:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleUpdateContext = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const token = localStorage.getItem('access_token');
      const response = await fetch('http://localhost:8000/api/context/', {
        method: 'PUT',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          device,
          location,
          current_goal: currentGoal,
          current_activity: currentActivity,
          emotional_state: emotionalState,
        }),
      });
      if (response.ok) {
        fetchContext();
      }
    } catch (error) {
      console.error('Error updating context:', error);
    }
  };

  return (
    <div className="container">
      <h1>Context Manager</h1>
      <div className="card">
        <h2>Current Context</h2>
        {loading ? (
          <p>Loading...</p>
        ) : (
          <form onSubmit={handleUpdateContext}>
            <div className="form-group">
              <label>Device</label>
              <input
                type="text"
                value={device}
                onChange={(e) => setDevice(e.target.value)}
                placeholder="e.g., laptop, phone, tablet"
              />
            </div>
            <div className="form-group">
              <label>Location</label>
              <input
                type="text"
                value={location}
                onChange={(e) => setLocation(e.target.value)}
                placeholder="e.g., home, office, cafe"
              />
            </div>
            <div className="form-group">
              <label>Current Goal</label>
              <textarea
                value={currentGoal}
                onChange={(e) => setCurrentGoal(e.target.value)}
                rows={3}
              />
            </div>
            <div className="form-group">
              <label>Current Activity</label>
              <input
                type="text"
                value={currentActivity}
                onChange={(e) => setCurrentActivity(e.target.value)}
              />
            </div>
            <div className="form-group">
              <label>Emotional State</label>
              <select
                value={emotionalState}
                onChange={(e) => setEmotionalState(e.target.value)}
              >
                <option value="">Select state...</option>
                <option value="happy">Happy</option>
                <option value="neutral">Neutral</option>
                <option value="stressed">Stressed</option>
                <option value="focused">Focused</option>
                <option value="tired">Tired</option>
              </select>
            </div>
            <button type="submit" className="btn btn-primary">
              Update Context
            </button>
          </form>
        )}
      </div>
    </div>
  );
}

export default Context;
