import uuid
from pydantic_ai import Agent, RunContext
from app.dependencies.dependencies import SupportDependencies
from app.models.schemas import SupportResult

support_agent = Agent(
    'openai:gpt-4o-mini',
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
async def block_card(ctx: RunContext[SupportDependencies] , customer_name: str ) -> str:
    return f"I'm sorry to hear that, {customer_name}. We are temporarily blocking your card to prevent unauthorized transactions."

@support_agent.tool
async def customer_balance(
    ctx: RunContext[SupportDependencies], include_pending: bool
) -> str:
    """Returns the customer's current account balance."""
    balance = await ctx.deps.db.customer_balance(
        id=ctx.deps.customer_id,
        include_pending=include_pending,
    )
    return f'${balance:.2f}'

@support_agent.tool
async def capture_customer_name(ctx: RunContext[SupportDependencies], customer_name: str) -> str:
    """Capture the customer's name for marketing purposes."""

    await ctx.deps.marketing_agent.run(f"Save customer name {customer_name} for ID {ctx.deps.customer_id}", deps=ctx.deps)

    tracking_id = str(uuid.uuid4())
