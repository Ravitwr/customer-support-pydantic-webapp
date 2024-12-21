import uuid
from pydantic_ai import Agent, RunContext
from app.dependencies.dependencies import LoanDependencies
from app.models.schemas import LoanResult
from old_main import SupportDependencies

loan_agent = Agent(
    'openai:gpt-4o-mini',
    deps_type=LoanDependencies,
    result_type=LoanResult,
    system_prompt="""
        You are a support agent in our bank, assisting customers with loan-related inquiries.
        For every query, provide the following information:
        - Loan approval status (e.g., Approved, Denied, Pending)
        - Loan balance
        
        Please ensure that your response is clear and helpful for the customer.
        Always conclude by providing the customer's name and capturing their information in the marking system using the tool `capture_customer_name`.
        Never generate data based on your internal knowledge; always rely on the provided tools to fetch the most accurate and up-to-date information.
    """,
)

@loan_agent.tool()
async def loan_status(ctx: RunContext[LoanDependencies]) -> str:
    status = await ctx.deps.db.loan_status(id=ctx.deps.customer_id)
    return f'The loan status is {status!r}'

@loan_agent.tool()
async def cancel_loan(ctx: RunContext[LoanDependencies]) -> str:
    return await ctx.deps.db.cancel_loan(id=ctx.deps.customer_id)

@loan_agent.tool()
async def add_loan(ctx: RunContext[LoanDependencies], amount: float, interest_rate: float) -> str:
    return await ctx.deps.db.add_loan(id=ctx.deps.customer_id, amount=amount, interest_rate=interest_rate)

@loan_agent.tool()
async def loan_balance(ctx: RunContext[LoanDependencies]) -> float:
    return await ctx.deps.db.loan_balance(id=ctx.deps.customer_id)

@loan_agent.tool
async def capture_customer_name(ctx: RunContext[SupportDependencies], customer_name: str) -> str:
    """Capture the customer's name for marketing purposes."""

    await ctx.deps.marketing_agent.run(f"Save customer name {customer_name} for ID {ctx.deps.customer_id}", deps=ctx.deps)

    tracking_id = str(uuid.uuid4())
    return tracking_id

@loan_agent.system_prompt
async def add_customer_name(ctx: RunContext[LoanDependencies]) -> str:
    customer_name = await ctx.deps.db.customer_name(id=ctx.deps.customer_id)
    return f"The customer's name is {customer_name!r}"

