# fastapi
from fastapi import APIRouter, Depends, HTTPException, Request

from application.use_cases.auth.refresh_token import RefreshToken

# dependencies
from presentation.dependencies.auth import get_refresh_token_use_case

router = APIRouter(prefix="/refresh-token")


@router.get("/")
def refresh_token(
    request: Request, use_case: RefreshToken = Depends(get_refresh_token_use_case)
):
    refresh_token = request.cookies.get("refresh_token")
    if not refresh_token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    result = use_case.execute(refresh_token)

    return result
