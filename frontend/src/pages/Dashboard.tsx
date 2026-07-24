import React from 'react';
import '../App.css';

interface DashboardProps {
  user: any;
}

function Dashboard({ user }: DashboardProps) {
  return (
    <div className="container">
      <h1>Dashboard</h1>
      <div className="grid">
        <div className="card">
          <h2>Welcome, {user?.username}!</h2>
          <p>This is your HXAI Dashboard. Here you can manage your memories, context, and sessions.</p>
        </div>
        <div className="card">
          <h2>Quick Stats</h2>
          <p>📝 Memories: 0</p>
          <p>📍 Sessions: 0</p>
          <p>🧠 Context Active: Yes</p>
        </div>
        <div className="card">
          <h2>Recent Activity</h2>
          <p>No recent activity yet. Start by creating a memory or session!</p>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
