import React, { useState } from "react";

function DocumentUploader() {
  const [status, setStatus] = useState("");

  const handleUpload = async (event) => {
    const files = event.target.files;
    const formData = new FormData();
    for (let i = 0; i < files.length; i++) {
      formData.append("files", files[i]);
    }

    try {
      const res = await fetch("http://127.0.0.1:8000/api/upload-documents", {
        method: "POST",
        body: formData,
      });
      const data = await res.json();
      setStatus(" Uploaded: " + JSON.stringify(data));
    } catch (e) {
      setStatus(" Error: " + e.message);
    }
  };

  return (
    <div>
      <h3>Upload Documents</h3>
      <input type="file" multiple onChange={handleUpload} />
      <p>{status}</p>
    </div>
  );
}

export default DocumentUploader;