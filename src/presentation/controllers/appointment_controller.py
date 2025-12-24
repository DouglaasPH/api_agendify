from datetime import date, datetime
from typing import Optional

# fastapi
from fastapi import APIRouter, Depends, Query

# schemas
from application.schemas.appointment import ToCreateAppointment

# use cases
from application.use_cases.appointment.create_appointment import CreateAppointment
from application.use_cases.appointment.list_appointment import ListAppointments
from application.use_cases.appointment.cancel_appointment import CancelAppointment
from application.use_cases.appointment.get_by_id_appointment import GetByIdAppointment

# dependencies
from presentation.dependencies.appointment import get_by_id_appointment, get_cancel_appointment, get_create_appointment_use_case, get_list_appointment
from presentation.dependencies.auth import get_current_customer, get_current_professional

# entities
from domain.entities.professional import Professional
from domain.entities.customer import Customer
from domain.entities.appointment import Appointment


router = APIRouter(prefix="/appointment")

@router.post("/customer")
def create_appointment_for_customer(
    data: ToCreateAppointment,
    current_customer: Customer = Depends(get_current_customer),
    use_case: CreateAppointment = Depends(get_create_appointment_use_case),
):
    use_case.execute(
        professional_id=data.professional_id,
        customer_id=current_customer.id,
        availability_id=data.availability_id
    )
    
    return { "msg": "Appointment created succesfully"}


@router.get("/customer")
def list_appointment_for_customer(
    current_customer: Customer = Depends(get_current_customer),
    use_case: ListAppointments = Depends(get_list_appointment),
):
    response = use_case.list_for_customer(current_customer.id)

    return response


@router.put("/customer/{appointment_id}")
def cancel_appointment_for_customer(
    appointment_id: int,
    current_customer: Customer = Depends(get_current_customer),
    use_case: CancelAppointment = Depends(get_cancel_appointment),
):
    use_case.cancel_by_customer(appointment_id, current_customer.id)

    return { "msg": "Appointment canceled succesfully" }


@router.get("/professional/list")
def list_appointment_for_professional(
    availability_id: Optional[int] = Query(None),
    status: Optional[str] = Query(None),
    customer_name: Optional[str] = Query(None),
    customer_email: Optional[str] = Query(None),
    date: Optional[date] = Query(None),
    start_time: Optional[datetime] = Query(None),
    end_time: Optional[datetime] = Query(None),
    slot_duration_minutes: Optional[int] = Query(None),
    current_professional: Professional = Depends(get_current_professional),
    use_case: ListAppointments = Depends(get_list_appointment),
):
    response = use_case.list_for_professional(
        professional_id=current_professional.id,
        availability_id=availability_id,
        status=status,
        customer_name=customer_name,
        customer_email=customer_email,
        date=date,
        start_time=start_time,
        end_time=end_time,
        slot_duration_minutes=slot_duration_minutes,
    )

    return response


@router.put("/professional/{appointment_id}")
def cancel_appointment_by_id_for_professional(
    appointment_id: int,
    current_professional: Professional = Depends(get_current_professional),
    use_case: CancelAppointment = Depends(get_cancel_appointment),
):
    use_case.cancel_by_professional(appointment_id, current_professional.id)

    return { "msg": "Appointment canceled succesfully" }


@router.put("/professional/{appointment_id}")
def get_appointment_by_id_for_professional(
    appointment_id: int,
    current_professional: Professional = Depends(get_current_professional),
    use_case: GetByIdAppointment = Depends(get_by_id_appointment),
):
    response = use_case.execute(current_professional.id, appointment_id)

    return response
