import React, { useEffect, useState } from "react";

function App() {
  const [status, setStatus] = useState({});
  const [recs, setRecs] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/battery/status")
      .then(res => res.json())
      .then(setStatus);
    fetch("http://localhost:8000/battery/recommendations")
      .then(res => res.json())
      .then(data => setRecs(data.Recs));
  }, []);

  return (
    <div style={{padding:"20px"}}>
      <h2>Dawnice Battery Admin Panel</h2>
      <p><b>SOC:</b> {status.SOC}%</p>
      <p><b>Voltage:</b> {status.Voltage} V</p>
      <p><b>Current:</b> {status.Current} A</p>
      <p><b>Load:</b> {status.Load} kW</p>
      <p><b>PV:</b> {status.PV} kW</p>

      <h3>⚡ Recommendations:</h3>
      <ul>
        {recs.map((r,i)=><li key={i}>{r}</li>)}
      </ul>
    </div>
  );
}

export default App;
