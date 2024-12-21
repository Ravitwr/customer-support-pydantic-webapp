from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.tables import Loan, Customer
from datetime import datetime

async def get_customer_name(db: AsyncSession, *, id: int) -> str | None:
    query = select(Customer.name).where(Customer.id == id)
    result = await db.execute(query)
    return result.scalar_one_or_none()

async def get_loan_status(db: AsyncSession, *, id: int) -> str | None:
    query = select(Loan.status).where(Loan.customer_id == id)
    result = await db.execute(query)
    return result.scalar_one_or_none()

async def cancel_loan(db: AsyncSession, *, id: int) -> str:
    query = select(Loan).where(Loan.customer_id == id, Loan.status == 'Active')
    result = await db.execute(query)
    loan = result.scalar_one_or_none()
    
    if not loan:
        raise ValueError(f"Customer {id} has no active loan.")
    
    loan.status = 'Canceled'
    await db.commit()
    return f"Loan for customer ID {id} has been canceled."

async def add_loan(db: AsyncSession, *, id: int, amount: float, interest_rate: float) -> str:
    customer = await db.get(Customer, id)
    if not customer:
        raise ValueError(f"Customer {id} not found.")
    
    new_loan = Loan(
        customer_id=id,
        amount=amount,
        interest_rate=interest_rate,
        balance=amount,
        created_at=datetime.utcnow()
    )
    db.add(new_loan)
    await db.commit()
    
    return f"Loan of ${amount} @ {interest_rate}% added for customer {id}."

async def get_loan_balance(db: AsyncSession, *, id: int) -> float:
    query = select(Loan.balance).where(Loan.customer_id == id)
    result = await db.execute(query)
    balance = result.scalar_one_or_none()
    
    if balance is None:
        raise ValueError(f"No loan for customer {id}.")
    return balance
