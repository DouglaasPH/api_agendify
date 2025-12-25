from datetime import date, datetime
from typing import Optional

# fastapi
from application.use_cases.availability.delete_availability import DeleteAvailability
from application.use_cases.availability.get_by_id_availability import GetByIdAvailability
from fastapi import APIRouter, Depends, Query

# schemas
from application.schemas.availability import ToCreateAvailability


# use cases
from application.use_cases.availability.create_availability import CreateAvailability
from application.use_cases.availability.list_availability import ListAvailability


# dependencies
from presentation.dependencies.availability import get_by_id_availability_use_case, get_create_availability_use_case, get_delete_availability_use_case, get_list_availability_use_case
from presentation.dependencies.auth import get_current_customer, get_current_professional

# entities
from domain.entities.professional import Professional
from domain.entities.customer import Customer


router = APIRouter(prefix="/availability")

@router.post("/professional/create")
def create_availability_for_professional(
    data: ToCreateAvailability,
    current_professional: Professional = Depends(get_current_professional),
    use_case: CreateAvailability = Depends(get_create_availability_use_case),
):
    use_case.execute(
        professional_id=current_professional.id,
        date=data.date,
        start_time=data.start_time,
        end_time=data.end_time,
        slot_duration_minutes=data.slot_duration_minutes,
    )
    
    return { "msg": "Availability created succesfully"}


@router.get("/professional/list")
def list_availability_for_professional(
    availability_id: Optional[int] = Query(None),
    date: Optional[date] = Query(None),
    start_time: Optional[datetime] = Query(None),
    end_time: Optional[datetime] = Query(None),
    slot_duration_minutes: Optional[int] = Query(None),
    status: Optional[str] = Query(None),
    current_professional: Professional = Depends(get_current_professional),
    use_case: ListAvailability = Depends(get_list_availability_use_case),
):
    print(current_professional.id)
    response = use_case.execute(
        professional_id=current_professional.id,
        availability_id=availability_id,
        date=date,
        start_time=start_time,
        end_time=end_time,
        slot_duration_minutes=slot_duration_minutes,
        status=status,
    )
    
    return response


@router.get("/professional/get/{availability_id}")
def get_availability_for_professional(
    availability_id: int,
    current_professional: Professional = Depends(get_current_professional),
    use_case: GetByIdAvailability = Depends(get_by_id_availability_use_case),
):
    response = use_case.execute(
        professional_id=current_professional.id,
        availability_id=availability_id,
    )
    
    return response


@router.put("/professional/delete/{availability_id}")
def delete_for_professional(
    availability_id: int,
    current_professional: Professional = Depends(get_current_professional),
    use_case: DeleteAvailability = Depends(get_delete_availability_use_case),
):
    response = use_case.execute(
        professional_id=current_professional.id,
        availability_id=availability_id,
    )
    
    return response


@router.get("/customer/list/{professional_id}")
def list_availability_for_customer(
    professional_id: int,
    current_customer: Customer = Depends(get_current_customer),
    use_case: ListAvailability = Depends(get_list_availability_use_case),
):
    response = use_case.execute(
        professional_id=professional_id,
        status="available",
    )
    
    return response
