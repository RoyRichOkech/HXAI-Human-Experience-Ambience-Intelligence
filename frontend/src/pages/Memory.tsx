import React, { useState, useEffect } from 'react';
import '../App.css';

function Memory() {
  const [memories, setMemories] = useState([]);
  const [loading, setLoading] = useState(false);
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [memoryType, setMemoryType] = useState('short_term');

  useEffect(() => {
    fetchMemories();
  }, []);

  const fetchMemories = async () => {
    setLoading(true);
    try {
      const token = localStorage.getItem('access_token');
      const response = await fetch('http://localhost:8000/api/memory/', {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });
      if (response.ok) {
        const data = await response.json();
        setMemories(data);
      }
    } catch (error) {
      console.error('Error fetching memories:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleCreateMemory = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const token = localStorage.getItem('access_token');
      const response = await fetch('http://localhost:8000/api/memory/', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          title,
          content,
          memory_type: memoryType,
        }),
      });
      if (response.ok) {
        setTitle('');
        setContent('');
        setMemoryType('short_term');
        fetchMemories();
      }
    } catch (error) {
      console.error('Error creating memory:', error);
    }
  };

  return (
    <div className="container">
      <h1>Memory Manager</h1>
      <div className="card">
        <h2>Create New Memory</h2>
        <form onSubmit={handleCreateMemory}>
          <div className="form-group">
            <label>Title</label>
            <input
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              required
            />
          </div>
          <div className="form-group">
            <label>Content</label>
            <textarea
              value={content}
              onChange={(e) => setContent(e.target.value)}
              rows={5}
              required
            />
          </div>
          <div className="form-group">
            <label>Memory Type</label>
            <select
              value={memoryType}
              onChange={(e) => setMemoryType(e.target.value)}
            >
              <option value="short_term">Short Term</option>
              <option value="long_term">Long Term</option>
              <option value="episodic">Episodic</option>
              <option value="semantic">Semantic</option>
              <option value="preference">Preference</option>
              <option value="habit">Habit</option>
            </select>
          </div>
          <button type="submit" className="btn btn-primary">
            Create Memory
          </button>
        </form>
      </div>
      <div className="card">
        <h2>Your Memories</h2>
        {loading ? (
          <p>Loading...</p>
        ) : memories.length === 0 ? (
          <p>No memories yet. Create one above!</p>
        ) : (
          <div>
            {memories.map((memory: any) => (
              <div key={memory.id} style={{ padding: '1rem', borderBottom: '1px solid #334155' }}>
                <h3>{memory.title}</h3>
                <p>{memory.content.substring(0, 100)}...</p>
                <small style={{ color: '#94a3b8' }}>Type: {memory.memory_type}</small>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default Memory;
