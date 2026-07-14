// Save login information
export const login = (username, password) => {

    if (username === "admin" && password === "admin123") {

        localStorage.setItem("login", "true");
        localStorage.setItem("username", username);

        return true;
    }

    return false;
};

// Logout
export const logout = () => {

    localStorage.removeItem("login");
    localStorage.removeItem("username");
    localStorage.removeItem("role");

};

// Check login
export const isAuthenticated = () => {

    return localStorage.getItem("login") === "true";

};

// Get Username
export const getUsername = () => {

    return localStorage.getItem("username");

};

// Get Role
export const getRole = () => {

    return localStorage.getItem("role");

};