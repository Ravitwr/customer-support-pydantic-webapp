import httpx
from typing import List
from fastapi import HTTPException
from app.core.config import settings

class TypefullyService:
    def __init__(self):
        self.api_key = settings.TYPEFULLY_API_KEY
        if not self.api_key:
            raise ValueError("TYPEFULLY_API_KEY environment variable is not set")
        self.base_url = "https://api.typefully.com"
        
    async def create_thread(self, tweets: List[str]) -> dict:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                        f"{self.base_url}/v1/drafts/",
                        headers={
                            "X-API-Key": self.api_key,
                            "Content-Type": "application/json"
                        },
                        json={
                            "content": "\n".join(tweets),
                            "threadify": True
                        }
                )
                
                if response.status_code != 200:
                    print(f"Typefully API error: {response.status_code} - {response.text}")
                    raise HTTPException(status_code=response.status_code, 
                                     detail=f"Typefully API error: {response.text}")
                    
                return response.json()
        except httpx.HTTPError as e:
            print(f"HTTP error: {e}")
            raise HTTPException(status_code=500, detail=str(e))
        except Exception as e:
            print(f"Unexpected error: {e}")
            raise HTTPException(status_code=500, detail=str(e))
