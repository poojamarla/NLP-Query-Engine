import React from "react";

function ResultsView({ results }) {
  if (!results) return null;
  return (
    <div>
      <h3>Results</h3>
      <pre>{JSON.stringify(results, null, 2)}</pre>
    </div>
  );
}

export default ResultsView;