from typing import List
from pydantic_ai import Agent, RunContext
from pydantic import BaseModel, Field
from app.core.config import settings

class CriticsFeedback(BaseModel):
    is_relevant: bool = Field(description="Whether the thread is relevant to the query")
    feedback: str = Field(description="Detailed feedback on how to improve the thread")

system_prompt="""You are a Twitter thread critic. Your task is to review threads and 
    provide constructive feedback on their relevance and quality. Focus on both content 
    accuracy and engagement. You will be provided with thread in <thread></thread> tags and the user query in <query></query> tags, and content in <content></content> tags.
   
    Please only return the output in specified format provided in <instructions></instructions> tags.
    Thread:
    <thread>
    {tweets}
    </thread>
    
    UserQuery:
    <query>
    {query}
    </query>
    
    Content:
    <content>
    {content}
    </content>

    <instructions>
    {instructions}
    </instructions>
    """
critics_agent = Agent(
    model='gemini-1.5-flash',
    result_type=CriticsFeedback,
)

async def review_thread(tweets: List[str],content: str, query: str) -> CriticsFeedback:
    instructions = "Please return the output in JSON format only with is_relevant and feedback as keys like this: { 'is_relevant': true, 'feedback': 'The thread is relevant to the query and provides valuable information.' }"
    user_prompt = system_prompt.format(query=query, tweets=tweets,content=content,instructions=instructions)
    result = await critics_agent.run(user_prompt)
    return result.data
