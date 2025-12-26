from abc import ABC, abstractmethod

from domain.entities.professional import Professional


class ProfessionalRepository(ABC):
    @abstractmethod
    def get_by_id(self, professional_id: int) -> Professional | None:
        pass

    def get_by_chat_code(self, chat_code: int) -> Professional | None:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Professional | None:
        pass

    @abstractmethod
    def save(self, professional: Professional) -> None:
        pass

    @abstractmethod
    def delete(self, professional_id: int) -> None:
        pass
