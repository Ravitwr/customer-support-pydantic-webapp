from dataclasses import dataclass
from app.repositories.customer import DatabaseConn
from app.repositories.loan import LoanDB
from pydantic_ai import Agent

@dataclass
class LoanDependencies:
    customer_id: int
    db: LoanDB
    marketing_agent: Agent

@dataclass
class SupportDependencies:
    customer_id: int
    db: DatabaseConn
    marketing_agent: Agent

@dataclass
class TriageDependencies:
    support_agent: Agent
    loan_agent: Agent
    customer_id: int