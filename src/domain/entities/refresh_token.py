from datetime import datetime, timezone

class RefreshToken:
    def __init__(
        self,
        id: int | None,
        professional_id: int,
        token: str,
        expires_at: datetime,
        is_revoked: bool = False
    ):
        self.id = id
        self.professional_id = professional_id
        self.token = token
        self.expires_at = expires_at
        self.is_revoked = is_revoked
    
    def is_valid(self) -> bool:
        return not self.is_revoked and self.expires_at > datetime.now(timezone.utc)
    
    def revoke(self):
        self.is_revoked = True
