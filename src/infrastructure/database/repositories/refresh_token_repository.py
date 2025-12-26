from sqlalchemy.orm import Session

from domain.entities.refresh_token import RefreshToken
from domain.repositories.refresh_token_repository import RefreshTokenRepository
from infrastructure.database.models.refresh_token import RefreshTokenModel


class RefreshTokenRepositorySQLAlchemy(RefreshTokenRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, token: RefreshToken) -> None:
        model = RefreshTokenModel(
            professional_id=token.professional_id,
            token=token.token,
            expires_at=token.expires_at,
            is_revoked=token.is_revoked,
        )
        self.session.add(model)
        self.session.commit()

    def get_by_token(self, token: str) -> RefreshToken | None:
        model = (
            self.session.query(RefreshTokenModel)
            .filter(RefreshTokenModel.token == token)
            .first()
        )

        if not model:
            return None

        return RefreshToken(
            id=model.id,
            professional_id=model.professional_id,
            token=model.token,
            expires_at=model.expires_at,
            is_revoked=model.is_revoked,
        )

    def revoke(self, token: str) -> None:
        model = (
            self.session.query(RefreshTokenModel)
            .filter(RefreshTokenModel.token == token)
            .first()
        )

        if model:
            model.is_revoked = True
            self.session.commit()

    def revoke_all_by_professional(self, professional_id: int) -> None:
        (
            self.session.query(RefreshTokenModel)
            .filter(
                RefreshTokenModel.professional_id == professional_id,
                ~RefreshTokenModel.is_revoked,
            )
            .update({"is_revoked": True})
        )

        self.session.commit()
