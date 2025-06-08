from fastapi import FastAPI, UploadFile, File, Form
from document_ingestion import extract_pdf_content
from llm_agent import DocumentQnAAgent
import os
from typing import List

app = FastAPI()
agent = DocumentQnAAgent(llm_api_key=os.getenv("GROQ_API_KEY"))

documents = {}

@app.post("/upload/")
async def upload_pdfs(files: List[UploadFile] = File(...)):
    results = []
    for file in files:
        file_path = f"temp_{file.filename}"
        with open(file_path, "wb") as f:
            f.write(await file.read())
        content = extract_pdf_content(file_path)
        documents[file.filename] = content
        os.remove(file_path)
        results.append({"filename": file.filename, "title": content["title"]})
    return {"message": "Files processed", "results": results}

@app.post("/ask/")
async def ask_question(question: str = Form(...), filename: str = Form(...)):
    content = documents.get(filename)
    if not content:
        return {"error": "Document not found. Please upload first."}
    answer = agent.ask(question, content)
    return {"answer": answer}
