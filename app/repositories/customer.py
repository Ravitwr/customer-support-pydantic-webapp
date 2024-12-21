from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.tables import Customer

async def get_customer_name(db: AsyncSession, *, id: int) -> str | None:
    query = select(Customer.name).where(Customer.id == id)
    result = await db.execute(query)
    return result.scalar_one_or_none()

async def get_customer_balance(db: AsyncSession, *, id: int) -> float:
    query = select(Customer.balance).where(Customer.id == id)
    result = await db.execute(query)
    balance = result.scalar_one_or_none()
    if balance is None:
        raise ValueError('Customer not found')
    return balance
