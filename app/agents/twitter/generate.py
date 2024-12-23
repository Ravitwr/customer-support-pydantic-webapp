from typing import List
from pydantic import BaseModel, Field
from pydantic_ai import Agent


class TwitterPostContent(BaseModel):
    tweets: List[str] = Field(description="List of tweets that form a thread")


system_prompt = """You are a Twitter thread generator working as a consultant in Tek-x.ai(Service Consulting Firm).
You would be given a blog post and you need to create a thread based on the blog.
Make sure that you are not just summarizing the blog but you are creating a thread based on the blog.

Each tweet should be under 280 characters and the thread should flow naturally. Maximum 3 tweets.
You will be provided with the user query in <query></query> tags, and the content gathered from google search in <content></content> tags.

Please create an engaging content for the user based on the query and the content and only return the output in specified format provided in <instructions></instructions> tags.

If the user query is not provided, please create a thread based on the content provided.
<query>
{query}
</query>

<content>
{content}
</content>

<instructions>
{instructions}
</instructions>

"""

post_agent = Agent(
    model='gemini-1.5-flash',
    result_type=TwitterPostContent,
)


async def create_thread(contents: str, query: str) -> TwitterPostContent:
    instructions = "You must respond in JSON format with tweets as a list of strings."
    user_prompt = system_prompt.format(query=query, content=contents, instructions=instructions)
    result = await post_agent.run(
        user_prompt=user_prompt
    )
    return result.data
