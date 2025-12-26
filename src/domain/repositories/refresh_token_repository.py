from abc import ABC, abstractmethod

from domain.entities.refresh_token import RefreshToken


class RefreshTokenRepository(ABC):
    @abstractmethod
    def save(self, token: RefreshToken) -> None:
        pass

    @abstractmethod
    def get_by_token(self, token: str) -> RefreshToken | None:
        pass

    @abstractmethod
    def revoke(self, token: str) -> None:
        pass

    def revoke_all_by_professional(self, professional_id: int) -> None:
        pass
