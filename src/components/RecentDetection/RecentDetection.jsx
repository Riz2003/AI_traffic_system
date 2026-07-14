import { useEffect, useState } from "react";
import API from "../../services/api";
import "./RecentDetection.css";

function RecentDetection() {

    const [history, setHistory] = useState([]);

    const loadHistory = () => {

        API.get("/history")
            .then((res) => {

                setHistory(res.data);

            })
            .catch((err) => {

                console.log(err);

            });

    };

    useEffect(() => {

        loadHistory();

        const interval = setInterval(loadHistory, 2000);

        return () => clearInterval(interval);

    }, []);

    return (

        <div className="history">

            <h2>Recent Detections</h2>

            <table>

                <thead>

                    <tr>

                        <th>ID</th>

                        <th>Vehicle</th>

                        <th>Confidence</th>

                        <th>Camera</th>

                        <th>Track ID</th>

                        <th>Date</th>

                        <th>Time</th>

                    </tr>

                </thead>

                <tbody>

                    {history.map((item) => (

                        <tr key={item.id}>

                            <td>{item.id}</td>

                            <td>{item.vehicle}</td>

                            <td>{item.confidence}%</td>

                            <td>{item.camera}</td>

                            <td>{item.track}</td>

                            <td>{item.date}</td>

                            <td>{item.time}</td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>

    );

}

export default RecentDetection;