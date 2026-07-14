import Navbar from "../../components/Navbar/Navbar";
import Sidebar from "../../components/Sidebar/Sidebar";
import DashboardCards from "../../components/DashboardCards/DashboardCards";
import LiveCamera from "../../components/LiveCamera/LiveCamera";
import VehicleChart from "../../components/VehicleChart/VehicleChart";
import VehiclePieChart from "../../components/VehiclePieChart/VehiclePieChart";
import VehicleTable from "../../components/VehicleTable/VehicleTable";
import Reports from "../../components/Reports/Reports";
import RecentDetection from "../../components/RecentDetection/RecentDetection";


function Dashboard(){

    return(

        <>

            <Sidebar/>

            <div style={{marginLeft:"260px"}}>

                <Navbar/>

                <DashboardCards/>

                <LiveCamera/>

                <VehicleChart/>

                <VehiclePieChart/>

                <VehicleTable/>

                <Reports/>
                <RecentDetection />

            </div>

        </>

    );

}

export default Dashboard;