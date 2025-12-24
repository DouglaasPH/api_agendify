# fastapi
from application.use_cases.auth.refresh_token import RefreshToken
from fastapi import APIRouter, Depends, Response, HTTPException, Request

# dependencies
from presentation.dependencies.auth import get_refresh_token_use_case


router = APIRouter(prefix="/refresh-token")


@router.post("/")
def refresh_token(
    response: Response,
    request: Request,
    use_case: RefreshToken = Depends(get_refresh_token_use_case)
):
    old_refresh_token = request.cookies.get("refresh_token")
    if not old_refresh_token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    result = use_case.execute(old_refresh_token)
    
    response.set_cookie(
        key="refresh_token",
        value=result["refresh_token"],
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=60*60*48,  # 2 days
        path="/",
        domain="localhost", 
    )
    
    return {
        "access_token": result["access_token"],
        "token_type": "bearer",
        "expires_in": result["expires_in"],
    }
