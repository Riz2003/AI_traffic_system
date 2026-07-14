import {
    Bar
} from "react-chartjs-2";

import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend
} from "chart.js";

import { useEffect, useState } from "react";
import API from "../../services/api";

ChartJS.register(
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend
);

function VehicleChart() {

    const [data, setData] = useState({
        cars: 0,
        bikes: 0,
        buses: 0,
        trucks: 0,
        bicycles: 0
    });

    useEffect(() => {

        const load = () => {

            API.get("/analytics")

                .then((res) => {

                    setData(res.data);

                });

        };

        load();

        const interval = setInterval(load, 2000);

        return () => clearInterval(interval);

    }, []);

    const chartData = {

        labels: [
            "Cars",
            "Bikes",
            "Buses",
            "Trucks",
            "Bicycles"
        ],

        datasets: [

            {

                label: "Vehicle Count",

                data: [

                    data.cars,

                    data.bikes,

                    data.buses,

                    data.trucks,

                    data.bicycles

                ]

            }

        ]

    };

    return (

        <div>

            <h2>Vehicle Analytics</h2>

            <Bar data={chartData} />

        </div>

    );

}

export default VehicleChart;