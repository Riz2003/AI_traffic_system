import "./Sidebar.css";

function Sidebar() {
  return (
    <div className="sidebar">

      <div className="logo">
        🚦 AI Traffic
      </div>

      <ul className="menu">

        <li>🏠 Dashboard</li>

        <li>📷 Live Camera</li>

        <li>🚗 Vehicle Detection</li>

        <li>📊 Analytics</li>

        <li>📑 Reports</li>

        <li>📜 Detection History</li>

        <li>👥 Users</li>

        <li>📹 Cameras</li>

        <li>⚙ Settings</li>

        <li>🚪 Logout</li>

      </ul>

    </div>
  );
}

export default Sidebar;