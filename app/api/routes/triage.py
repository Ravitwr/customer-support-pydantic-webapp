from fastapi import APIRouter, HTTPException
from app.models.schemas import UserQuery, TriageResult
from app.agents.triage import triage_agent
from app.agents.support import support_agent
from app.agents.loan import loan_agent
from app.dependencies.dependencies import TriageDependencies

router = APIRouter()

@router.post("/triage", response_model=TriageResult)
async def triage_query(payload: UserQuery):
    customer_id = 123
    deps = TriageDependencies(
        support_agent=support_agent,
        loan_agent=loan_agent,
        customer_id=customer_id
    )

    try:
        result = await triage_agent.run(payload.query, deps=deps)
        return result.data
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail={e})
