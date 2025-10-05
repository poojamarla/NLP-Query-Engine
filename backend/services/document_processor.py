import os
import docx
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter

class DocumentProcessor:
    def __init__(self):
        # Using a small but effective embedding model
        self.model = None
        self.documents = []       
        self.embeddings = []      
        
    def _load_model(self):
        if self.model is None:
            self.model = SentenceTransformer("all-MiniLM-L6-v2")
            print("Embedding model loaded")

  
    # Step 1: Load Documents
    def process_documents(self, file_paths: list):
        self._load_model()
        all_texts = []
        for file in file_paths:
            ext = os.path.splitext(file)[-1].lower()
            if ext == ".pdf":
                all_texts.append(self._read_pdf(file))
            elif ext == ".docx":
                all_texts.append(self._read_docx(file))
            elif ext == ".txt":
                all_texts.append(self._read_txt(file))
            elif ext == ".csv":
                all_texts.append(self._read_txt(file))  # treat CSV as text
            else:
                print(f"Skipping unsupported file: {file}")

        combined = "\n".join(all_texts)
        chunks = self._chunk_text(combined)
        self.documents = chunks

        # Generate embeddings
        self.embeddings = self.model.encode(chunks, convert_to_tensor=True)

        return len(chunks)

  
    # Step 2: Text Readers
    def _read_pdf(self, file_path):
        text = ""
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text

    def _read_docx(self, file_path):
        text = ""
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text

    def _read_txt(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

 
    # Step 3: Chunking
    def _chunk_text(self, text: str, chunk_size=500, overlap=50):
        splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
        return splitter.split_text(text)

  
    # Step 4: Query Search
    def search(self, query: str, top_k=3):
        self._load_model()
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        scores = (self.embeddings @ query_embedding.T)  # cosine similarity matrix
        top_idx = scores.argsort(descending=True)[:top_k]
        top_results = [self.documents[i] for i in top_idx]
        return top_results
   