import "./DashboardCards.css";
import { useEffect, useState } from "react";
import API from "../../services/api";

function DashboardCards() {

    const [data, setData] = useState({
        total: 0,
        cars: 0,
        bikes: 0,
        buses: 0,
        trucks: 0,
        bicycles: 0,
    });

    useEffect(() => {

        API.get("/dashboard")
            .then((response) => {
                setData(response.data);
            })
            .catch((error) => {
                console.error("API Error:", error);
            });

    }, []);

    return (

        <div className="cards-container">

            <div className="card">
                <h3>Total Vehicles</h3>
                <h1>{data.total}</h1>
            </div>

            <div className="card">
                <h3>Cars</h3>
                <h1>{data.cars}</h1>
            </div>

            <div className="card">
                <h3>Bikes</h3>
                <h1>{data.bikes}</h1>
            </div>

            <div className="card">
                <h3>Buses</h3>
                <h1>{data.buses}</h1>
            </div>

            <div className="card">
                <h3>Trucks</h3>
                <h1>{data.trucks}</h1>
            </div>

            <div className="card">
                <h3>Bicycles</h3>
                <h1>{data.bicycles}</h1>
            </div>

        </div>

    );
}

export default DashboardCards;