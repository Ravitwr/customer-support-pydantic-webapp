from fastapi import APIRouter, Depends, HTTPException
from app.core.database.transaction import get_db
from app.models.schemas import UserQuery, TriageResult
from app.agents.triage import triage_agent
from app.agents.support import support_agent
from app.agents.loan import loan_agent
from app.dependencies.dependencies import TriageDependencies
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter()

@router.post("/triage", response_model=TriageResult)
async def triage_query(
    payload: UserQuery,
    customer_id: int,
    db: AsyncSession = Depends(get_db)
):
    deps = TriageDependencies(
        support_agent=support_agent,
        loan_agent=loan_agent,
        customer_id=customer_id,
        db=db
    )

    try:
        result = await triage_agent.run(payload.query, deps=deps)
        return result.data
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail={e})
