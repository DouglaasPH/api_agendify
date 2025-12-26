import datetime as dt

from pydantic import BaseModel


class ToCreateAvailability(BaseModel):
    date: dt.date
    start_time: dt.datetime
    end_time: dt.datetime
    slot_duration_minutes: int
