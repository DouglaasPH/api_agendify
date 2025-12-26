from domain.entities.customer import Customer, CustomerStatus
from domain.repositories.customer_repository import CustomerRepository
from infrastructure.security.token_service import TokenService


class RegisterOrLoginCustomer:
    def __init__(
        self, customer_repository: CustomerRepository, token_service: TokenService
    ):
        self.customer_repository = customer_repository
        self.token_service = token_service

    def execute(self, name: str, email: str):
        if not name or not email:
            raise ValueError("invalid credentials.")

        customer = self.customer_repository.get_by_email(email)

        print(customer)

        if not customer:
            customer = Customer(
                id=None, name=name, email=email, status=CustomerStatus.active
            )
            self.customer_repository.save(customer)

        access_token = self.token_service.create_access_token(
            subject=str(customer.id),
            role="customer",
        )

        return {
            "access_token": access_token,
            "customer_data": {
                "id": customer.id,
                "name": customer.name,
                "email": customer.email,
            },
        }
