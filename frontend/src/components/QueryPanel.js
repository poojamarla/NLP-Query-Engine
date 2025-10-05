import React, { useState } from "react";

function QueryPanel({ setResults }) {
  const [query, setQuery] = useState("");

  const runQuery = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/api/query", {
        method: "POST",
        body: new URLSearchParams({ query }),
      });
      const data = await response.json();
      setResults(data);
    } catch (e) {
      setResults({ error: e.message });
    }
  };

  return (
    <div>
      <h3>Ask a Query</h3>
      <input
        type="text"
        placeholder="e.g. How many employees do we have?"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        style={{ width: "400px" }}
      />
      <button onClick={runQuery}>Run</button>
    </div>
  );
}

export default QueryPanel;