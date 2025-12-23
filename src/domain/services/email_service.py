from abc import ABC, abstractmethod

class EmailService(ABC):
    @abstractmethod
    async def send_welcome_email(self, username: str, email: str) -> None:
        pass

    @abstractmethod
    async def send_verification_email(self, verification_link: str, email: str) -> None:
        pass

    @abstractmethod
    async def send_login_email(self, username: str, email: str) -> None:
        pass

    @abstractmethod
    async def send_password_reset_email(self, username: str, email: str, link: str) -> None:
        pass

    @abstractmethod
    async def send_email_change_confirmation(
        self,
        username: str,
        old_email: str,
        new_email: str,
        link: str
    ) -> None:
        pass
