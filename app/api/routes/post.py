from fastapi import APIRouter, HTTPException
from app.models.twitter import URLInput, TwitterThread, TwitterResponse
from app.services.tavily_service import TavilyService
from app.services.typefully_service import TypefullyService
from app.agents.twitter import generate, critics, finalize

router = APIRouter()
tavily_service = TavilyService()
typefully_service = TypefullyService()

@router.post("/generate")
async def generate_thread(input_data: URLInput) -> TwitterThread:
    # Extract content from URLs
    contents = await tavily_service.extract_content_from_urls(input_data.urls)
    
    # Generate initial thread
    thread_generator = await generate.create_thread(contents, input_data.query)
    
    print(thread_generator, "thread_generator")
    # Get feedback from critics
    feedback = await critics.review_thread(thread_generator.tweets,contents, input_data.query)
    
    # # Finalize thread based on feedback
    final_thread = await finalize.finalize_thread(thread_generator.tweets, feedback.feedback)
    
    return TwitterThread(tweets=final_thread.tweets)

@router.post("/submit")
async def submit_thread(thread: TwitterThread) -> TwitterResponse:
    try:
        # Add logging to debug the incoming payload
        print("Received thread data:", thread.dict())
        
        # Ensure tweets are in correct format before sending to Typefully
        if not thread.tweets or not isinstance(thread.tweets, list):
            raise HTTPException(status_code=400, detail="Invalid tweet format. Expected list of tweets")
            
        result = await typefully_service.create_thread(thread.tweets)
        return TwitterResponse(
            thread=thread,
            status="success"
        )
    except ValueError as ve:
        # Handle JSON parsing errors
        raise HTTPException(status_code=400, detail=f"Invalid request format: {str(ve)}")
    except Exception as e:
        # Log the full error for debugging
        print(f"Error in submit_thread: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
