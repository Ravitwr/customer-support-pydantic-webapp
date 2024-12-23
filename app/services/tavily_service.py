from typing import List
from tavily import AsyncTavilyClient
from app.core.config import settings

class TavilyService:
    def __init__(self):
        self.client = AsyncTavilyClient(api_key=settings.TAVILY_API_KEY)
    
    async def extract_content_from_urls(self, urls: List[str]) -> str:
        contents = []
        for url in urls:
            try:
                response = await self.client.extract(url)
                contents = response.get("results", [])
                return contents[0].get("raw_content","")
            except Exception as e:
                print(f"Error extracting content from {url}: {str(e)}")
                continue
        return ""
