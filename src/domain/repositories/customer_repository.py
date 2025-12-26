from abc import ABC, abstractmethod

from domain.entities.customer import Customer


class CustomerRepository(ABC):
    @abstractmethod
    def get_by_id(self, customer_id: int) -> Customer | None:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Customer | None:
        pass

    @abstractmethod
    def save(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def delete(self, customer_id: int) -> None:
        pass
