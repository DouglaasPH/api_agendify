# fastapi
from fastapi import APIRouter, Depends

# schemas
from application.schemas.customer import CustomerInput

# use cases
from application.use_cases.customer.register_customer import RegisterOrLoginCustomer
from application.use_cases.customer.login_by_id_customer import LoginByIdCustomer

# dependencies
from presentation.dependencies.customer import (
    get_login_by_id_customer_use_case,
    get_register_costumer_use_case,
)


router = APIRouter(prefix="/customer")


@router.post("/")
def register_or_login(
    data: CustomerInput,
    use_case: RegisterOrLoginCustomer = Depends(get_register_costumer_use_case),
):
    response = use_case.execute(
        name=data.name,
        email=data.email,
    )

    return response


@router.post("/{customer_id}")
def login_with_customer_id(
    customer_id: int,
    use_case: LoginByIdCustomer = Depends(get_login_by_id_customer_use_case),
):
    response = use_case.execute(customer_id)

    return response
