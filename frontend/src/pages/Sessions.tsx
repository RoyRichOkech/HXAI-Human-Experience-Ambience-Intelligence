import React, { useState, useEffect } from 'react';
import '../App.css';

function Sessions() {
  const [sessions, setSessions] = useState([]);
  const [loading, setLoading] = useState(false);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');

  useEffect(() => {
    fetchSessions();
  }, []);

  const fetchSessions = async () => {
    setLoading(true);
    try {
      const token = localStorage.getItem('access_token');
      const response = await fetch('http://localhost:8000/api/sessions/', {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });
      if (response.ok) {
        const data = await response.json();
        setSessions(data);
      }
    } catch (error) {
      console.error('Error fetching sessions:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleCreateSession = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const token = localStorage.getItem('access_token');
      const response = await fetch('http://localhost:8000/api/sessions/', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          title,
          description,
        }),
      });
      if (response.ok) {
        setTitle('');
        setDescription('');
        fetchSessions();
      }
    } catch (error) {
      console.error('Error creating session:', error);
    }
  };

  return (
    <div className="container">
      <h1>Sessions</h1>
      <div className="card">
        <h2>Create New Session</h2>
        <form onSubmit={handleCreateSession}>
          <div className="form-group">
            <label>Title</label>
            <input
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
            />
          </div>
          <div className="form-group">
            <label>Description</label>
            <textarea
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              rows={3}
            />
          </div>
          <button type="submit" className="btn btn-primary">
            Create Session
          </button>
        </form>
      </div>
      <div className="card">
        <h2>Your Sessions</h2>
        {loading ? (
          <p>Loading...</p>
        ) : sessions.length === 0 ? (
          <p>No sessions yet. Create one above!</p>
        ) : (
          <div>
            {sessions.map((session: any) => (
              <div key={session.id} style={{ padding: '1rem', borderBottom: '1px solid #334155' }}>
                <h3>{session.title || 'Untitled Session'}</h3>
                <p>{session.description}</p>
                <small style={{ color: '#94a3b8' }}>Created: {new Date(session.created_at).toLocaleDateString()}</small>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default Sessions;
