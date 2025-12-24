from abc import ABC

from sqlalchemy.orm import Session

from domain.entities.refresh_token import RefreshToken
from infrastructure.database.models.refresh_token import RefreshTokenModel


class RefreshTokenRepositorySQLAlchemy(ABC):
    def __init__(self, session: Session):
        self.session = session

    def save(self, token: RefreshToken) -> None:
        model = RefreshTokenModel(
            profession_id=token.professional_id,
            token=token.token,
            expires_at=token.expires_at,
            is_revoked=token.is_revoked
        )
        self.session.add(model)
        self.session.commit()

    def get_by_token(self, token: str) -> RefreshToken | None:
        model = (
            self.session
            .query(RefreshTokenModel)
            .filter(RefreshTokenModel.token == token)
            .first()
        )

        if not model:
            return None

        return RefreshToken(
            id=model.id,
            user_id=model.user_id,
            token=model.token,
            expires_at=model.expires_at,
            is_revoked=model.is_revoked,
        )

    def revoke(self, token: str) -> None:
        model = (
            self.session
            .query(RefreshTokenModel)
            .filter(RefreshTokenModel.token == token)
            .first()
        )

        if model:
            model.is_revoked = True
            self.session.commit()
    
    def revoke_all_by_professional(self, professional_id: int) -> None:
        self.session.query(RefreshTokenModel).filter(
            RefreshTokenModel.profession_id == professional_id,
            RefreshTokenModel.is_revoked == False,
        ).update({"is_revoked": True})
