import React, { useState } from "react";

function DatabaseConnector() {
  const [conn, setConn] = useState("");
  const [status, setStatus] = useState("");

  const connectDB = async () => {
    try {
      const formData = new FormData();
      formData.append("connection_string", conn);

      const res = await fetch("http://127.0.0.1:8000/api/connect-database", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();
      setStatus("Connected: " + JSON.stringify(data));
    } catch (e) {
      setStatus("❌ Error: " + e.message);
    }
  };

  return (
    <div>
      <h3>Database Connection</h3>
      <input
        type="text"
        placeholder="sqlite:///backend/test.db"
        value={conn}
        onChange={(e) => setConn(e.target.value)}
        style={{ width: "400px" }}
      />
      <button onClick={connectDB}>Connect</button>
      <p>{status}</p>
    </div>
  );
}

export default DatabaseConnector;