import arxiv

def search_arxiv(query):
    search = arxiv.Search(query=query, max_results=1)
    for result in search.results():
        return {
            "title": result.title,
            "summary": result.summary,
            "pdf_url": result.pdf_url,
        }
    return None
