import uuid
from pydantic_ai import Agent, RunContext
from app.dependencies.dependencies import SupportDependencies
from app.models.schemas import SupportResult
from app.repositories.customer import get_customer_balance
from app.core.config import settings

support_agent = Agent(
    settings.LLM_MODEL,
    deps_type=SupportDependencies,
    result_type=SupportResult,
    system_prompt="""
        You are a support agent in our bank, give the 
        customer support and judge the risk level of their query.
        Reply using the customer's name.
        Additionally, always capture the customer's name in our marketing system using the tool `capture_customer_name`, regardless of the query type.
        At the end of your response, make sure to capture the customer's name to maintain proper records.
    """,
)

@support_agent.tool()
async def _block_card(ctx: RunContext[SupportDependencies] , customer_name: str ) -> str:
    return f"I'm sorry to hear that, {customer_name}. We are temporarily blocking your card to prevent unauthorized transactions."

@support_agent.tool
async def _customer_balance(ctx: RunContext[SupportDependencies]) -> str:
    """Returns the customer's current account balance."""
    balance = await get_customer_balance(ctx.deps.db, id=ctx.deps.customer_id)
    
    return f'${balance:.2f}'

@support_agent.tool
async def _capture_customer_name(ctx: RunContext[SupportDependencies], customer_name: str) -> str:
    """Capture the customer's name for marketing purposes."""

    await ctx.deps.marketing_agent.run(f"Save customer name {customer_name} for ID {ctx.deps.customer_id}", deps=ctx.deps)

    tracking_id = str(uuid.uuid4())
    return tracking_id
