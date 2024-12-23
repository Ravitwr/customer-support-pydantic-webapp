from typing import List
from pydantic_ai import Agent, RunContext
from pydantic import BaseModel, Field

class FinalizedThread(BaseModel):
    tweets: List[str] = Field(description="Final version of the tweets")

system_prompt="""You will be given a set of tweets and the feedback of the agents after reviewing the tweets.
    Please improve the tweets based on the feedback and return the improved tweets in JSON format as the instructions are provided in <instructions></instructions> tags.
    
    The tweets are in <tweets></tweets> tags.

    The feedback is in <feedback></feedback> tags.
    
    Please make the tweets like a human would write who has a consulting background and trying to engage the audience and potential customers


    <tweets>
    {tweets}
    </tweets>

    <feedback>
    {feedback}
    </feedback>

    <instructions>
    {instructions}
    </instructions>
    """

finalizer_agent = Agent(
    model='gemini-1.5-flash',
    result_type=FinalizedThread,
)

async def finalize_thread(tweets: List[str], feedback: str) -> FinalizedThread:
    instructions = "Please return the output in JSON format only with tweets as key like this: { 'tweets': ['tweet1', 'tweet2', 'tweet3'] }"
    format_tweets = "\n".join([f"{tweet}" for tweet in tweets])
    user_prompt = system_prompt.format(tweets=format_tweets, feedback=feedback, instructions=instructions)
    result = await finalizer_agent.run(
        user_prompt=user_prompt
    )
    return result.data
