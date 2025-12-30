from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import class_mapper

from infrastructure.database.models.appointment import AppointmentModel
from infrastructure.database.models.availability import AvailabilityModel
from infrastructure.database.models.customer import CustomerModel
from infrastructure.database.models.professional import ProfessionalModel
from infrastructure.database.models.refresh_token import RefreshTokenModel
from presentation.controllers import (
    appointment_controller,
    availability_controller,
    customer_controller,
    professional_controller,
    refresh_token_controller,
)

print("MODELS REGISTRADOS:")
print(class_mapper(ProfessionalModel))
print(class_mapper(RefreshTokenModel))
print(class_mapper(CustomerModel))
print(class_mapper(AvailabilityModel))
print(class_mapper(AppointmentModel))


app = FastAPI(title="Agendify API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(appointment_controller.router)
app.include_router(availability_controller.router)
app.include_router(customer_controller.router)
app.include_router(professional_controller.router)
app.include_router(refresh_token_controller.router)

