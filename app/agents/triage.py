from pydantic_ai import Agent, RunContext
from pydantic_ai.result import RunResult
from app.dependencies.dependencies import LoanDependencies, SupportDependencies, TriageDependencies
from app.models.schemas import TriageResult
from app.agents.marketing import marketing_agent
from typing import Any
from app.core.config import settings

triage_agent = Agent(
    settings.LLM_MODEL,
    deps_type=TriageDependencies,
    system_prompt=(
        'You are a triage agent in our bank, responsible for directing customer queries to the appropriate department. '
        'For each query, determine whether it is related to support (e.g., balance, card, account-related queries) or loan services (e.g., loan status, application, and loan-related inquiries). '
        'If the query is related to support, direct the customer to the support team with an appropriate response. '
        'If the query is related to loans, direct the customer to the loan department with a relevant response. '
        'If the query is unclear or does not fit into either category, politely inform the customer and suggest they ask about loans or support. '
        'Always ensure that the response is clear, concise, and provides direction to the right department for further assistance.'
        'Never generate data based on your internal knowledge; always rely on the provided tools to fetch the most accurate and up-to-date information.'
    ),
    result_type=TriageResult,
)

@triage_agent.tool
async def _call_support_agent(ctx: RunContext[TriageDependencies], prompt: str) -> RunResult[Any]:
    print(f"Calling support agent with prompt: {prompt}")
    support_deps = SupportDependencies(customer_id=ctx.deps.customer_id, db=ctx.deps.db, marketing_agent=marketing_agent)

    return await ctx.deps.support_agent.run(prompt, deps=support_deps)

@triage_agent.tool
async def _call_loan_agent(ctx: RunContext[TriageDependencies], quest: str) -> RunResult[Any]:
    print(f"Calling loan agent with prompt: {quest}")
    loan_deps = LoanDependencies(customer_id=ctx.deps.customer_id, db=ctx.deps.db, marketing_agent=marketing_agent)

    return await ctx.deps.loan_agent.run(quest, deps=loan_deps)
