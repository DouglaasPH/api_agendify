from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine, Base
from controllers import auth, appointment, availabilities, customers


@asynccontextmanager
async def lifespan(app: FastAPI):
    from models.appointments import Appointments                  # noqa
    from models.availabilities import Availabilities              # noqa
    from models.users import Users                                # noqa
    from models.refresh_tokens import RefreshToken                # noqa
    from models.customers import Customers                        # noqa
    
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(auth.router)
app.include_router(appointment.router)
app.include_router(availabilities.router)
app.include_router(customers.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)