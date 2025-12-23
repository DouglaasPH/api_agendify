from passlib.context import CryptContext

class PasswordHasher:
    def __init__(self):
        self._context = CryptContext(
            schemes=["bcrypt"],
            deprecated="auto"
        )
    
    def hash(self, plain_password: str) -> str:
        if not plain_password:
            raise ValueError("Password cannot be empty")
        
        return self._context(plain_password)
    
    def verify(self, plain_password: str, hashed_password: str) -> bool:
        if not plain_password or not hashed_password:
            return False
        
        return self._context.verify(plain_password, hashed_password)