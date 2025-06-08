# Document Q&A AI Agent

## Overview
This project is an enterprise-ready Document Q&A AI Agent that leverages open LLM APIs (GROQ, OpenAI, etc.) to answer questions about uploaded PDF documents. It supports multi-modal document ingestion, accurate content extraction, and advanced querying, including Arxiv API integration for research paper lookup.

## Features
- **Multiple PDF Uploads:** Upload and manage multiple PDF documents in a single or multiple requests.
- **Content Extraction:** Extracts titles, abstracts, sections, tables, and references from PDFs. Preserves equations and tables where possible.
- **NLP-Powered Q&A:** Ask questions about any uploaded document, including direct lookups, summarization, and extraction of evaluation results (e.g., accuracy, F1-score).
- **Arxiv API Integration:** (Bonus) Search and retrieve research papers from Arxiv by description.
- **Enterprise-Grade:** Context handling, secure API key management, and response optimization.

## Setup Instructions

1. **Clone the repository**
   ```sh
   git clone <your-repo-url>
   cd project_practice
   ```

2. **Create and activate a virtual environment**
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure API Keys**
   - Edit the `.env` file and set your `GROQ_API_KEY` (or other LLM provider key).

5. **Run the FastAPI server**
   ```sh
   uvicorn main:app --reload
   ```

6. **Open the API docs**
   - Go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to interact with the API.

## Usage

### Upload PDFs
- Use the `/upload/` endpoint to upload one or more PDF files.
- Each file is processed and stored for querying.

### Ask Questions
- Use the `/ask/` endpoint.
- Provide your question and the filename of the PDF you want to query.
- The agent will return a concise, accurate answer using the LLM.

### Arxiv Lookup (Bonus)
- Use the `search_arxiv` function in `arxiv_lookup.py` to search for papers by description.
- You can test this via the provided `test_arxiv.py` script.

## Example
```python
from arxiv_lookup import search_arxiv
result = search_arxiv("transformer neural networks")
print(result)
```

## Security & Best Practices
- API keys are managed via `.env` and never hardcoded.
- All file uploads are handled securely and temporarily stored.
- LLM responses are optimized for enterprise use (context, concise answers).

## Demo
- See `demo_video.mp4` (to be added) for a walkthrough of the system, including PDF upload, Q&A, and Arxiv lookup.

## License
MIT License

---
**For any questions or improvements, please open an issue or pull request.**
