import os
from dotenv import load_dotenv
from groq import Groq  # Or OpenAI, depending on your LLM provider

class DocumentQnAAgent:
    def __init__(self, llm_api_key=None):
        load_dotenv()
        if llm_api_key is None:
            llm_api_key = os.getenv("GROQ_API_KEY")
        self.llm = Groq(api_key=llm_api_key)

    def ask(self, question, document_content):
        prompt = f"""
        You are an AI assistant for document Q&A.
        Document: {document_content['title']}
        Content: {document_content['full_text']}
        Question: {question}
        Answer concisely and accurately.
        """
        response = self.llm.chat.completions.create(
            model="llama3-70b-8192",  # Example model
            messages=[{"role": "user", "content": prompt}],
            max_tokens=512,
            temperature=0.2,
        )
        return response.choices[0].message.content.strip()
