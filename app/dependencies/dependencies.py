from dataclasses import dataclass
from pydantic_ai import Agent
from sqlalchemy.ext.asyncio import AsyncSession

@dataclass
class LoanDependencies:
    customer_id: int
    db: AsyncSession
    marketing_agent: Agent

@dataclass
class SupportDependencies:
    customer_id: int
    db: AsyncSession
    marketing_agent: Agent

@dataclass
class TriageDependencies:
    support_agent: Agent
    loan_agent: Agent
    customer_id: int
    db: AsyncSession