import "./Reports.css";

import jsPDF from "jspdf";
import autoTable from "jspdf-autotable";

import * as XLSX from "xlsx";

import { saveAs } from "file-saver";

function Reports(){

const vehicles=[

{
time:"10:15",
vehicle:"Car",
camera:"Camera 1",
confidence:"98%"
},

{
time:"10:18",
vehicle:"Truck",
camera:"Camera 2",
confidence:"96%"
},

{
time:"10:20",
vehicle:"Bike",
camera:"Camera 1",
confidence:"97%"
}

];

const exportPDF=()=>{

const doc=new jsPDF();

doc.text("Vehicle Detection Report",14,20);

autoTable(doc,{

head:[[

"Time",

"Vehicle",

"Camera",

"Confidence"

]],

body:vehicles.map(v=>[

v.time,

v.vehicle,

v.camera,

v.confidence

])

});

doc.save("Vehicle_Report.pdf");

};

const exportExcel=()=>{

const worksheet=XLSX.utils.json_to_sheet(vehicles);

const workbook=XLSX.utils.book_new();

XLSX.utils.book_append_sheet(

workbook,

worksheet,

"Vehicles"

);

const excelBuffer=XLSX.write(

workbook,

{

bookType:"xlsx",

type:"array"

}

);

const fileData=new Blob(

[excelBuffer],

{

type:"application/octet-stream"

}

);

saveAs(

fileData,

"Vehicle_Report.xlsx"

);

};

const printReport=()=>{

window.print();

};

return(

<div className="report-card">

<h2>Reports</h2>

<button onClick={exportPDF}>

Export PDF

</button>

<button onClick={exportExcel}>

Export Excel

</button>

<button onClick={printReport}>

Print Report

</button>

</div>

);

}

export default Reports;