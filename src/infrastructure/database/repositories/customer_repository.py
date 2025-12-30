from sqlalchemy.orm import Session

from domain.entities.customer import Customer, CustomerStatus
from domain.repositories.customer_repository import CustomerRepository
from infrastructure.database.models.customer import CustomerModel


class CustomerRepositorySQLAlchemy(CustomerRepository):

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, customer_id: int) -> Customer | None:
        model = (
            self.session.query(CustomerModel)
            .filter(CustomerModel.id == customer_id)
            .filter(CustomerModel.status != CustomerStatus.deleted.value)
            .first()
        )

        if not model:
            return None

        return self._to_entity(model)

    def get_by_email(self, email: str) -> Customer | None:
        model = (
            self.session.query(CustomerModel)
            .filter(CustomerModel.email == email)
            .filter(CustomerModel.status != CustomerStatus.deleted.value)
            .first()
        )

        if not model:
            return None

        return self._to_entity(model)

    def save(self, customer: Customer) -> None:
        model = CustomerModel(
            id=customer.id,
            name=customer.name,
            email=customer.email,
        )

        self.session.merge(model)
        self.session.commit()

    def delete(self, customer_id: int) -> None:
        self.session.query(CustomerModel).filter_by(id=customer_id).delete()
        self.session.commit()

    def _to_entity(self, model: CustomerModel) -> Customer:
        return Customer(
            id=model.id, name=model.name, email=model.email, status=model.status
        )
