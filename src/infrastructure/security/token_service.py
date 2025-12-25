from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError

from infrastructure.settings import settings

class TokenService:
    ISSUER = "api_agendify"
    AUDIENCE = "api_agendify"
    
    def __init__(self):
        self.secret_key = settings.SECRET_KEY
        self.algorithm = settings.ALGORITHM
        self.expire_miutes = settings.ACCESS_TOKEN_EXPIRE_MINUTES
        
    def create_token_for_register_professional(self, subject: dict, expires_delta: timedelta):
        return jwt.encode(subject, self.secret_key, algorithm=self.algorithm)
    
    def create_access_token(self, subject: str, role: str) -> str:
        datetime_now = datetime.now(timezone.utc)
        expiration_datetime = datetime_now + timedelta(minutes=self.expire_miutes)
        
        payload = {
            "sub": subject,                       # "customer_id" | "professional_id"
            "role": role,                         # "customer" | "professional"
            "iss": self.ISSUER, # api_agendify
            "aud": self.AUDIENCE, # api_agendify
            "iat": int(datetime_now.timestamp()),
            "exp": int(expiration_datetime.timestamp())
        }
        
        token_str = jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
        
        return {
            "access_token": token_str,
            "expires_in": self.expire_miutes * 60,
            "token_type": "Bearer"
        }
    
    def create_temporary_token(self, payload: dict, expires_minutes: int) -> str:
        now = datetime.now(timezone.utc)
        payload["iat"] = int(now.timestamp())
        payload["exp"] = int((now + timedelta(minutes=expires_minutes)).timestamp())
        payload["iss"] = self.ISSUER
        payload["aud"] = self.AUDIENCE

        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
        
    def decode_token(self, token: str):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm], audience=self.AUDIENCE, issuer=self.ISSUER)
            return payload
        except JWTError:
            raise ValueError("Invalid or expired token")
        
    def get_subject(self, token) -> str:
        payload = self.decode_token(token)
        return payload.get("sub")
