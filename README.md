# 🧠 NLP Query Engine for Employee Data

A full‑stack AI Engineering project that lets users query both structured and unstructured employee data using **natural language**.  
The system discovers database schemas automatically, understands plain‑English user queries, and returns results from SQL tables, documents, or both.

## 🚀 Features

- 🗃️ **Dynamic Schema Discovery** – automatically detects tables, columns, relationships.
- 💬 **Natural Language Query Engine** – converts plain English into SQL queries.
- 📄 **Document Processing** – uploads & searches resumes, reviews, contracts.
- 🔀 **Hybrid Queries** – combines database + document search results.
- ⚡ **Performance Optimizations** – caching, pagination, async operations.
- 🧩 **Clean Architecture** – FastAPI backend & React frontend.

## 🏗️ Project Structure

nlp-query-engine/<br>
│<br>
├── backend/<br>
│   ├── main.py<br>
│   ├── services/<br>
│   │   ├── schema_discovery.py<br>
│   │   ├── query_engine.py<br>
│   │   ├── document_processor.py<br>
│   ├── docs/<br>
│   ├── test.db<br>
│<br>
├── frontend/<br>
│   ├── src/<br>
│   │   ├── components/<br>
│   │   │   ├── DatabaseConnector.js<br>
│   │   │   ├── DocumentUploader.js<br>
│   │   │   ├── QueryPanel.js<br>
│   │   │   ├── ResultsView.js<br>
│   │   ├── App.js<br>
│<br>
├── requirements.txt<br>
├── README.md<br>
└── technical_documentation.pdf

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/nlp-query-engine.git
cd nlp-query-engine
```

### 2. Backend Setup (FastAPI)
```bash
python -m venv venv
venv\Scripts\activate       # (Windows)
# or source venv/bin/activate  (Mac/Linux)
pip install -r requirements.txt
uvicorn backend.main:app --reload
```
Backend runs on http://127.0.0.1:8000

### 3. Frontend Setup (React)
```bash
cd frontend
npm install
npm start
```
Frontend runs on http://localhost:3000


## 🧪 Using the Application

1. **Connect to Database**  
   - Use connection string: `sqlite:///backend/test.db`
   - Click “Connect” — schema appears in result.

2. **Upload Documents**  
   - Choose `.txt`, `.pdf`, `.docx`, or `.csv` files.
   - Upload and wait for “Uploaded Successfully”.

3. **Ask a Query**  
   - Example queries:  
     - `How many employees do we have?`  
     - `What is the average salary by department?`  
     - `Find resumes of Python developers`  
     - `Compare employees with resumes`

4. **View Results**  
   - SQL results shown in tables  
   - Document results show relevant text snippets.
  
## 💻 Tech Stack

**Backend:** FastAPI • SQLAlchemy • SQLite • SentenceTransformers  
**Frontend:** React • JavaScript • HTML/CSS  
**Language:** Python 3.8+  
**Libraries:** pydantic • langchain • PyPDF2 • python-docx  

## 🖼️ UI Screenshots

![App Screenshot](docs/screenshot_ui.png)

## 🎥 Demo Video
Watch the full walkthrough on Loom: [Insert Loom Video URL Here]

## 🧩 Example Queries & Results

**Input:**  
`How many employees do we have?`

**Output:**  
```json
{
  "status": "ok",
  "query_type": "sql",
  "results": [[4]]
}
```

Input:
Find resumes of Python developers

Output:
```json
{
  "status": "ok",
  "query_type": "document",
  "results": [
    "Alice Johnson is a Python developer with 5 years of backend experience...",
    "Resume summary: Software Engineer with expertise in Python..."
  ]
}

```

## 🙌 Acknowledgments
Developed as part of the AI Engineering Assignment for learning and demonstrating  
query understanding, schema discovery, and hybrid AI systems.



## 👩‍💻 Author
**Pooja Marlashikari**  
Feel free to reach me at: poojamarla2001@gmail.com  
