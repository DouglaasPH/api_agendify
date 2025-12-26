from fastapi import Depends
from sqlalchemy.orm import Session

from application.use_cases.customer.login_by_id_customer import LoginByIdCustomer
from application.use_cases.customer.register_customer import RegisterOrLoginCustomer
from infrastructure.database.database import get_db
from infrastructure.database.repositories.customer_repository import (
    CustomerRepositorySQLAlchemy,
)
from infrastructure.security.token_service import TokenService


def get_register_costumer_use_case(
    db: Session = Depends(get_db),
) -> RegisterOrLoginCustomer:
    return RegisterOrLoginCustomer(
        customer_repository=CustomerRepositorySQLAlchemy(db),
        token_service=TokenService(),
    )


def get_login_by_id_customer_use_case(
    db: Session = Depends(get_db),
) -> LoginByIdCustomer:
    return LoginByIdCustomer(
        customer_repository=CustomerRepositorySQLAlchemy(db),
        token_service=TokenService(),
    )
