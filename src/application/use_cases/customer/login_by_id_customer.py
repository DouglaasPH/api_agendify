from domain.repositories.customer_repository import CustomerRepository
from infrastructure.security.token_service import TokenService


class LoginByIdCustomer:
    def __init__(
        self, customer_repository: CustomerRepository, token_service: TokenService
    ):
        self.customer_repository = customer_repository
        self.token_service = token_service

    def execute(self, customer_id: int):
        customer = self.customer_repository.get_by_id(customer_id)

        if not customer:
            raise ValueError("Customer not found")

        access_token = self.token_service.create_access_token(
            subject=str(customer.id),
            role="customer",
        )

        return {
            "token_type": "bearer",
            "access_token": access_token,
            "customer_data": {
                "id": customer.id,
                "name": customer.name,
                "email": customer.email,
            },
        }
