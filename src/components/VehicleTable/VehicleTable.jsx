import "./VehicleTable.css";

function VehicleTable() {

    const vehicles = [

        {
            id:1,
            time:"10:20:15",
            vehicle:"Car",
            confidence:"98%",
            camera:"Camera 1",
            status:"Detected"
        },

        {
            id:2,
            time:"10:21:10",
            vehicle:"Truck",
            confidence:"96%",
            camera:"Camera 1",
            status:"Detected"
        },

        {
            id:3,
            time:"10:21:42",
            vehicle:"Bike",
            confidence:"97%",
            camera:"Camera 2",
            status:"Detected"
        },

        {
            id:4,
            time:"10:22:05",
            vehicle:"Bus",
            confidence:"95%",
            camera:"Camera 1",
            status:"Detected"
        }

    ];

    return (

        <div className="table-card">

            <h2>Vehicle Detection History</h2>

            <table>

                <thead>

                    <tr>

                        <th>ID</th>
                        <th>Time</th>
                        <th>Vehicle</th>
                        <th>Confidence</th>
                        <th>Camera</th>
                        <th>Status</th>

                    </tr>

                </thead>

                <tbody>

                    {vehicles.map((item)=>(
                        <tr key={item.id}>

                            <td>{item.id}</td>

                            <td>{item.time}</td>

                            <td>{item.vehicle}</td>

                            <td>{item.confidence}</td>

                            <td>{item.camera}</td>

                            <td>{item.status}</td>

                        </tr>
                    ))}

                </tbody>

            </table>

        </div>

    );

}

export default VehicleTable;