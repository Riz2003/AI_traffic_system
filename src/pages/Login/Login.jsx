import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { login } from "../../services/auth.js";
import "./Login.css";

function Login() {

    const navigate = useNavigate();

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleLogin = () => {

        if (login(username, password)) {

            navigate("/dashboard");

        } else {

            alert("Invalid Username or Password");

        }

    };

    return (

        <div className="login">

            <div className="login-box">

                <h1>AI Traffic Monitoring System</h1>

                <input
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />

                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />

                <button onClick={handleLogin}>
                    Login
                </button>

            </div>

        </div>

    );

}

export default Login;