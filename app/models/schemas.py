from pydantic import BaseModel, Field
from typing import Optional, Union

class UserQuery(BaseModel):
    query: str = Field(..., description="Customer's request or question.")

class SupportResult(BaseModel):
    support_advice: str
    block_card: bool
    risk: int
    customer_tracking_id: str

class LoanResult(BaseModel):
    loan_approval_status: str
    loan_balance: float
    customer_tracking_id: str

class TriageResult(BaseModel):
    department: Optional[str]
    response: Optional[Union[LoanResult, SupportResult]]
    text_response: Optional[str]
