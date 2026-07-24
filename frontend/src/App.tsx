import React, { useState, useEffect } from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route, Link, Navigate } from 'react-router-dom';
import Login from './pages/Login';
import Register from './pages/Register';
import Dashboard from './pages/Dashboard';
import Memory from './pages/Memory';
import Context from './pages/Context';
import Sessions from './pages/Sessions';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [user, setUser] = useState(null);

  useEffect(() => {
    // Check if user is already logged in
    const token = localStorage.getItem('access_token');
    if (token) {
      setIsAuthenticated(true);
      // Fetch user profile
      fetchUserProfile(token);
    }
  }, []);

  const fetchUserProfile = async (token: string) => {
    try {
      const response = await fetch('http://localhost:8000/api/users/me', {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });
      if (response.ok) {
        const userData = await response.json();
        setUser(userData);
      } else {
        // Token is invalid
        localStorage.removeItem('access_token');
        setIsAuthenticated(false);
      }
    } catch (error) {
      console.error('Error fetching user profile:', error);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    setIsAuthenticated(false);
    setUser(null);
  };

  return (
    <Router>
      <div className="app">
        {isAuthenticated && user && (
          <nav className="navbar">
            <div className="navbar-brand">
              <h1>HXAI</h1>
              <p>Human Experience Ambient Intelligence</p>
            </div>
            <div className="navbar-links">
              <Link to="/dashboard">Dashboard</Link>
              <Link to="/sessions">Sessions</Link>
              <Link to="/memory">Memory</Link>
              <Link to="/context">Context</Link>
            </div>
            <div className="navbar-user">
              <span>{user.username}</span>
              <button onClick={handleLogout} className="logout-btn">
                Logout
              </button>
            </div>
          </nav>
        )}
        <Routes>
          {!isAuthenticated ? (
            <>
              <Route
                path="/"
                element={<Navigate to="/login" replace />}
              />
              <Route
                path="/login"
                element={<Login setIsAuthenticated={setIsAuthenticated} setUser={setUser} />}
              />
              <Route
                path="/register"
                element={<Register setIsAuthenticated={setIsAuthenticated} setUser={setUser} />}
              />
            </>
          ) : (
            <>
              <Route path="/" element={<Navigate to="/dashboard" replace />} />
              <Route path="/dashboard" element={<Dashboard user={user} />} />
              <Route path="/sessions" element={<Sessions />} />
              <Route path="/memory" element={<Memory />} />
              <Route path="/context" element={<Context />} />
            </>
          )}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
