import "./Navbar.css";
import { useNavigate } from "react-router-dom";
import { logout, getUsername } from "../../services/auth.js";

function Navbar() {

    const navigate = useNavigate();

    const handleLogout = () => {
        logout();
        navigate("/");
    };

    return (
        <header className="navbar">

            <div className="navbar-left">
                <h2>Monitoring System</h2>
            </div>

            <div className="navbar-center">
                <input
                    type="text"
                    placeholder="Search Vehicles..."
                />
            </div>

            <div className="navbar-right">

                <button className="icon-btn">
                    🔔
                </button>

                <button className="icon-btn">
                    ⚙️
                </button>

                <div className="profile">

                    <img
                        src="https://i.pravatar.cc/40"
                        alt="Admin"
                    />

                    <div className="profile-info">
                        <span>{getUsername()}</span>
                        <small>Administrator</small>
                    </div>

                </div>

                <button
                    className="logout-btn"
                    onClick={handleLogout}
                >
                    Logout
                </button>

            </div>

        </header>
    );
}

export default Navbar;