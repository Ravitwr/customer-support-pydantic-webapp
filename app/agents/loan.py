import uuid
from pydantic_ai import Agent, RunContext
from app.dependencies.dependencies import LoanDependencies, SupportDependencies
from app.models.schemas import LoanResult
from app.repositories.customer import get_customer_name
from app.repositories.loan import add_loan, cancel_loan, get_loan_balance, get_loan_status
from app.core.config import settings

loan_agent = Agent(
    settings.LLM_MODEL,
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
async def _loan_status(ctx: RunContext[LoanDependencies]) -> str:
    status = await get_loan_status(ctx.deps.db, id=ctx.deps.customer_id)
    return f'The loan status is {status!r}'

@loan_agent.tool()
async def _cancel_loan(ctx: RunContext[LoanDependencies]) -> str:
    return await cancel_loan(ctx.deps.db, id=ctx.deps.customer_id)

@loan_agent.tool()
async def _add_loan(ctx: RunContext[LoanDependencies], amount: float, interest_rate: float) -> str:
    print(ctx.deps.customer_id)
    print(f"Adding loan of {amount} for customer {ctx.deps.customer_id}")
    return await add_loan(ctx.deps.db, id=ctx.deps.customer_id, amount=amount, interest_rate=interest_rate)

@loan_agent.tool()
async def _loan_balance(ctx: RunContext[LoanDependencies]) -> float:
    return await get_loan_balance(ctx.deps.db, id=ctx.deps.customer_id)

@loan_agent.tool
async def _capture_customer_name(ctx: RunContext[LoanDependencies], customer_name: str) -> str:
    """Capture the customer's name for marketing purposes."""
    print(f"Capturing customer name {customer_name} for ID {ctx.deps.customer_id}")
    await ctx.deps.marketing_agent.run(f"Save customer name {customer_name} for ID {ctx.deps.customer_id}", deps=ctx.deps)

    tracking_id = str(uuid.uuid4())
    return tracking_id

@loan_agent.system_prompt
async def _get_customer_name(ctx: RunContext[LoanDependencies]) -> str:
    customer_name = await get_customer_name(ctx.deps.db, id=ctx.deps.customer_id)
    return f"The customer's name is {customer_name!r}"

