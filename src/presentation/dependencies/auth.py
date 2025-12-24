from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from domain.services.email_service import EmailService

from application.use_cases.auth.refresh_token import RefreshToken
from application.use_cases.auth.generate_verification_token import GenerateVerificationToken

from infrastructure.database.repositories.refresh_token_repository import RefreshTokenRepositorySQLAlchemy
from infrastructure.security.password_hasher import PasswordHasher
from infrastructure.security.token_service import TokenService
from presentation.dependencies.database import get_db
from infrastructure.database.repositories.professional_repository import ProfessionalRepositorySQLAlchemy
from infrastructure.database.repositories.customer_repository import CustomerRepositorySQLAlchemy

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_customer(
    token: str = Depends(oauth2_scheme),
    db = Depends(get_db)
):
    token_service = TokenService()
    payload = TokenService.decode_token(token)
    
    if payload.get("role") != "customer":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detal="Not a customer token"
        )
    
    customer_id = payload.get("sub")
    
    if not customer_id:
        raise HTTPException(status_code=401, detal="Invalid token")
    
    customer_repository = CustomerRepositorySQLAlchemy(db)
    customer = customer_repository.get_by_id(customer_id)
    
    if not customer:
        raise HTTPException(status_code=401, detail="Customer not found")
    
    if customer.status == "deleted":
        raise HTTPException(status_code=403, detail="Deleted customer")
    
    return customer


def get_current_professional(
    token: str = Depends(oauth2_scheme),
    db = Depends(get_db)
):
    token_service = TokenService()
    payload = TokenService.decode_token(token)
    
    if payload.get("role") != "professional":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detal="Not a professional token"
        )
    
    professional_id = payload.get("sub")
    
    if not professional_id:
        raise HTTPException(status_code=401, detal="Invalid token")
    
    professional_repository = ProfessionalRepositorySQLAlchemy(db)
    professional = professional_repository.get_by_id(professional_id)
    
    if not professional:
        raise HTTPException(status_code=401, detail="Professional not found")
    
    if professional.status == "deleted":
        raise HTTPException(status_code=403, detail="Deleted professional")
    
    return professional


def get_refresh_token_use_case() -> RefreshToken:
    return RefreshToken(
        refresh_token_repository=RefreshTokenRepositorySQLAlchemy(),
        professional_repository=ProfessionalRepositorySQLAlchemy(),
        token_service=TokenService(),
    )

def get_generate_verification_token_use_case() -> GenerateVerificationToken:
    return GenerateVerificationToken(
        password_hasher=PasswordHasher(),
        token_service=TokenService(),
        email_service=EmailService(),
    )
