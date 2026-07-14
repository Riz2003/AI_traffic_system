import {
    Pie
} from "react-chartjs-2";

import {

    Chart as ChartJS,

    ArcElement,

    Tooltip,

    Legend

} from "chart.js";

ChartJS.register(

    ArcElement,

    Tooltip,

    Legend

);

function VehiclePieChart() {

    const data={

        labels:[

            "Cars",

            "Bikes",

            "Buses",

            "Trucks",

            "Bicycles"

        ],

        datasets:[

            {

                data:[

                    120,

                    80,

                    30,

                    40,

                    20

                ],

                backgroundColor:[

                    "#2563eb",

                    "#22c55e",

                    "#f59e0b",

                    "#ef4444",

                    "#8b5cf6"

                ]

            }

        ]

    };

    return(

        <div className="chart-card">

            <h2>

                Vehicle Distribution

            </h2>

            <Pie data={data}/>

        </div>

    );

}

export default VehiclePieChart;