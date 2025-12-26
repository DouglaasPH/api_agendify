import datetime as dt

from pydantic import BaseModel


class ToCreateAppointment(BaseModel):
    professional_id: int
    availability_id: int
    customer_id: int


class ListAppointments(BaseModel):
    professional_id: int
    availability_id: int
    status: str
    customer: str
    customer_email: str
    date: dt.date
    start_time: dt.datetime
    end_time: dt.datetime
    slot_duration_minutes: int
