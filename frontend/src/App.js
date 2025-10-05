import React, { useState } from "react";
import DatabaseConnector from "./components/DatabaseConnector";
import DocumentUploader from "./components/DocumentUploader";
import QueryPanel from "./components/QueryPanel";
import ResultsView from "./components/ResultsView";

function App() {
  const [results, setResults] = useState(null);

  return (
    <div style={{padding:"20px"}}>
      <h2>🔎 NLP Query Engine</h2>
      <DatabaseConnector />
      <DocumentUploader />
      <QueryPanel setResults={setResults} />
      <ResultsView results={results} />
    </div>
  );
}

export default App;