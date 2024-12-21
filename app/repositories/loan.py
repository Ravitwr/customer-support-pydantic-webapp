class LoanDB:
    @classmethod
    async def customer_name(cls, *, id: int) -> str | None:
        if id == 123:
            return 'John'

    @classmethod
    async def loan_status(cls, *, id: int) -> str | None:
        if id == 123:
            return 'Active'
        elif id == 124:
            return 'Paid off'
        elif id == 125:
            return 'Defaulted'
        else:
            return None

    @classmethod
    async def cancel_loan(cls, *, id: int) -> str:
        if id == 123:
            return f"Loan for customer ID {id} has been canceled."
        else:
            raise ValueError(f"Customer {id} has no active loan.")

    @classmethod
    async def add_loan(cls, *, id: int, amount: float, interest_rate: float) -> str:
        if id == 123:
            return f"Loan of ${amount} @ {interest_rate}% added for customer {id}."
        else:
            raise ValueError(f"Customer {id} not found.")

    @classmethod
    async def loan_balance(cls, *, id: int) -> float | None:
        if id == 123:
            return 5000.0
        elif id == 124:
            return 0.0
        else:
            raise ValueError(f"No loan for customer {id}.")
