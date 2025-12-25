from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from presentation.controllers import (
    appointment_controller,
    availability_controller,
    customer_controller,
    professional_controller,
    refresh_token_controller,
)

from sqlalchemy.orm import class_mapper
from infrastructure.database.models import *

print("MODELS REGISTRADOS:")
print(class_mapper(ProfessionalModel))
print(class_mapper(RefreshTokenModel))
print(class_mapper(CustomerModel))
print(class_mapper(AvailabilityModel))
print(class_mapper(AppointmentModel))


app = FastAPI(title="Agendify API")

app.include_router(appointment_controller.router)
app.include_router(availability_controller.router)
app.include_router(customer_controller.router)
app.include_router(professional_controller.router)
app.include_router(refresh_token_controller.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)